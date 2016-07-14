from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckOut a container
@app.route('/ma/ContainerInfo/<chemId>/<conId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maContainerInfo(chemId, conId):
  chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  container = containersModel.Containers.get(containersModel.Containers.conId == conId)
  if request.method =="GET":
    return render_template("views/ma/ContainerInfoView.html", config = config, container = container, chemical = chemical)
