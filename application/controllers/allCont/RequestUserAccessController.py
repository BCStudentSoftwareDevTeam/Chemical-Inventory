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
@app.route('/RequestUserAccess/', methods = ['GET', 'POST'])
def RequestUserAccess():
  # User authorization
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  if userLevel == -1 or user == -1:
    abort(403)
  print user.username, userLevel
  
  if request.method == "POST":
    data = request.form
    modelData, extraData = sortPost(data, Users)
    modelData['auth_level'] = "systemUser"
    modelData['created_by'] = user.username
    modelData['username'] = modelData['username'].lower()
    Users.create(**modelData)
  return render_template("views/RequestUserAccessView.html", config = config, userConfig = userConfig)
    
  
 
 