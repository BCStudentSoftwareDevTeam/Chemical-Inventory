from application import app
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Display containers that are checked out
@app.route('/sa/CheckedOut/', methods = ['GET'])
@require_role('systemAdmin')
def CheckedOut():
  containers = Containers.select().where(Containers.checkedOut == True) #Get a list of all containers that are set to checked out
  return render_template("views/sa/CheckedOutView.html", 
                         config = config,
                         contConfig = contConfig,
                         containers = containers)

