from application import app
from application.models import *
from application.config import *
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
  print user.username, userLevel
  
  return render_template("views/ma/ViewUserView.html", config = config, authLevel = userLevel)

