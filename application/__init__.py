import uuid
from flask import Flask, session, redirect, url_for, request, abort

app = Flask(__name__)

# Import all of the controllers for your application
from application.config import config
from application.absolutepath import getAbsolutePath

app.secret_key = config['flask']['secretKey']

# Set up the administrative interface
########################################
from flask_admin import expose, Admin, AdminIndexView
from application.logic.validation import doesUserHaveRole

class RoleVerifiedAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self): 
      if doesUserHaveRole("admin"):
        # print "Role Verified"
        return super(RoleVerifiedAdminIndexView, self).index()
      else:
        # print "No Role Verified"
        return redirect("/", code = 302)

admin = Admin(app,
              name = config['application']['title'],
              index_view = RoleVerifiedAdminIndexView(),
              template_mode = 'bootstrap3')



# Store the username (which will have been set by the webserver) into the config.
# FIXME: This is temporary. Fix with proper code for running under Apache/Shibboleth
from application.logic.validation import getUsernameFromEnv
config['flask']['username'] = getUsernameFromEnv()


def authUser(env):
    envK = "eppn"
    if (envK in env):
      # we need to sanitize the environment variable
      # TODO: this looks like a function that can be taken out
      return env[envK].split("@")[0].split('/')[-1].lower()
    elif ("DEBUG" in config) and config['sys']["debug"]:
      old_username =  config["DEBUG"]["user"]
      converted_user = config["DEBUG"]["user"].split('@')[0].split('/')[-1].lower()
      #TODO: log
      return config["DEBUG"]["user"].split('@')[0].split('/')[-1].lower()
    else:
      return None

@app.before_request
def queryCount():
    if session:
        session['querycount'] = 0

from peewee import BaseQuery
if 'show_queries' in config and config['show_queries']:
    old_execute = BaseQuery.execute
    def new_execute(*args, **kwargs):
        if session:
            if 'querycount' not in session:
                session['querycount'] = 0

            session['querycount'] += 1
            print("**Running query {}**".format(session['querycount']))
            print(args[0])

        return old_execute(*args, **kwargs)
    BaseQuery.execute = new_execute

# Import these last to avoid circular references
from application.controllers import *
