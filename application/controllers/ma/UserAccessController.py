from application import app
from application.models.usersModel import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Approve and Deny Users
@app.route('/ma/UserAccess/', methods = ['GET', 'POST'])
@require_role('admin')
def UserAccess():
  if request.method == "POST":
    data = request.form
    modelData, extraData = sortPost(data,Users)
    Users.create(**modelData)
  return render_template("views/ma/UserAccessView.html", config = config, userConfig = userConfig)

