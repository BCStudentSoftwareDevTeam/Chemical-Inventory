from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckOut a container
@app.route('/ma/CheckOut/<chemName>/<conId>/', methods = ['GET', 'POST'])
@require_role('admin')

def maCheckOut(conId):
  

def maCheckOut(chemName, conId):

  container = containersModel.Containers.get(conId = conId)
  print container
  return render_template("views/ma/CheckOutView.html", config = config, container = container, chemName = chemName)

