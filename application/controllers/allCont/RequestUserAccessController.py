from application import app
from application.models.usersModel import *
from application.config import *
from application.logic.sortPost import *
from application.logic.getAuthUser import AuthorizedUser

from flask import \
    render_template, \
    request, \
    redirect, \
    url_for

# PURPOSE: superUser or Staff requesting for a student to have access to the system.
@app.route('/fa/RequestUserAccess/', methods = ['GET', 'POST'])
def RequestUserAccess():
  # User authorization
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  print user.username, userLevel
  
  if request.method == "POST":
    data = request.form
    modelData, extraData = sortPost(data, Users)
    Users.create(**modelData)
  return render_template("views/fa/RequestUserAccessView.html", config = config, userConfig = userConfig)
    
  
 
 