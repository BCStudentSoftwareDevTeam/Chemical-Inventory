from application import app
from application.models.usersModel import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    url_for, \
    abort

# PURPOSE: Approve and Deny Users
@app.route('/UserAccess/', methods = ['GET', 'POST'])
def UserAccess():
  # User authorization
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  print user.username, userLevel
  
  if userLevel == "admin":
    if request.method == "POST":
      data = request.form
      modelData, extraData = sortPost(data,Users)
      Users.create(**modelData)
    return render_template("views/ma/UserAccessView.html", config = config, userConfig = userConfig, authLevel = userLevel)
  else:
    abort(403)