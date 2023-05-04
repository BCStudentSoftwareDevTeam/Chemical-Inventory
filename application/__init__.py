# This must come first in this particular file.
from flask import Flask
from flask import session, redirect, url_for, request, abort
from flask_session import Session

app = Flask(__name__)
sess = Session()

# Import all of the controllers for your application
from application.controllers import *
from application.config import config
from application.absolutepath import getAbsolutePath

# We need to track session information for using the
# admin console. This is not fully understood yet.
# The admin console does not work without it, though.
import uuid
if config['flask']['secretKey'] in ["UUID", "RANDOM"]:
  app.secret_key = uuid.uuid4()
else:
  app.secret_key = "secretsecretsecret"

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = getAbsolutePath('flask_session')
sess.init_app(app)

# Set up the administrative interface
import flask_admin as admin
from flask_admin import expose
from flask_admin.contrib.peewee import ModelView
from application.logic.validation import doesUserHaveRole

class RoleVerifiedAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self): 
      if doesUserHaveRole("admin"):
        # print "Role Verified"
        return super(RoleVerifiedAdminIndexView, self).index()
      else:
        # print "No Role Verified"
        return redirect("/", code = 302)

admin = admin.Admin(app,
                    name = config['application']['title'],
                    index_view = RoleVerifiedAdminIndexView(),
                    template_mode = 'bootstrap3')
from application.models import classes
for c in classes:
  # print "Adding ModelView to {0}".format(c)
  admin.add_view(ModelView(c))

# Store the username (which will have been set by the webserver) into the config.
# FIXME: This is temporary. Fix with proper code for running under Apache/Shibboleth
import os
from application.logic.validation import getUsernameFromEnv
config['flask']['username'] = getUsernameFromEnv()


# This hook ensures that a connection is opened to handle any queries
# generated by the request. Opens every database, which is not ideal,
# but because we don't know which will be used...
@app.before_request
def _db_connect():
  for db in config['databases']['dynamic'].keys():
    theDB = config['databases']['dynamic'][db]['theDB']
    theDB.connect()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_appcontext
def _db_close(exc):
  for db in config['databases']['dynamic'].keys():
    theDB = config['databases']['dynamic'][db]['theDB']
    if not theDB.is_closed():
        theDB.close()

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
