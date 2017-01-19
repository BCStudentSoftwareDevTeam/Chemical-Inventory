from application import app
from application.models import *
from application.config import *
from application.models.usersModel import *
from application.logic.getAuthUser import AuthorizedUser

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: View all the user and add new users 
@app.route('/ViewUser/', methods = ['GET', 'POST'])
def ViewUser():
  # User authorization
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  if userLevel == -1 or user == -1:
    abort(403)
  print user.username, userLevel
  usersList = Users.select().where(Users.approve == True)
  if request.method == "POST":
    data = request.form
    if 'auth_level' in data:
      #Updating selected user to a new selected auth_level
      updateQuery = Users.update(auth_level = data['auth_level']).where(Users.username == data['username'])
      updateQuery.execute()
    else:
      removeQuery = Users.delete().where(Users.username == data['username'])
      removeQuery.execute()
  return render_template("views/ViewUserView.html", config = config, authLevel = userLevel, usersList = usersList)

