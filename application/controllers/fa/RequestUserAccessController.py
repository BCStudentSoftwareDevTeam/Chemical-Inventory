from application import app
from application.models.usersModel import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    redirect, \
    url_for

# PURPOSE: Faculty or Staff requesting for a student to have access to the system.
@app.route('/fa/RequestUserAccess/', methods = ['GET', 'POST'])
@require_role('faculty')
def RequestUserAccess():
  if request.method == "POST":
    data = request.form
    modelData, extraData = sortPost(data, Users)
    Users.create(**modelData)
  return render_template("views/fa/RequestUserAccessView.html", config = config, userConfig = userConfig)
    
  
 
 