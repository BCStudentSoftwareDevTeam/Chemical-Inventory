from application import app
from application.models import *
from application.config import *
from application.models.usersModel import *
from application.logic.getAuthUser import AuthorizedUser
import time

from flask import \
    render_template, \
    request, \
    url_for, \
    flash

# PURPOSE: View all the user and add new users 
@app.route('/AddUser/', methods = ['GET', 'POST'])
def AddUser():
  # User authorization
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  if userLevel == -1 or user == -1:
    abort(403)
  print user.username, userLevel
  if userLevel == "admin":
    if request.method == "POST":
      flashMessage, flashFormat = createUser(request.form, user.username, True) # createUser function located in usersModel.py
      flash(flashMessage, flashFormat)
  date = time.strftime("%d/%m/%Y")
  return render_template("views/AddUserView.html", config = config, authLevel = userLevel, date = date)

