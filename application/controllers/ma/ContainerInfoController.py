from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role
from datetime import *

from flask import \
    render_template, \
    request, \
    redirect, \
    url_for

# PURPOSE: CheckOut a container
@app.route('/ma/ContainerInfo/<chemId>/<conId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maContainerInfo(chemId, conId):
  chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  container = containersModel.Containers.get(containersModel.Containers.conId == conId)
  if request.method =="POST":
    if request.form['dispose'] == "Dispose of this Container":
      container.disposalDate = datetime.now()
      container.save()
      return redirect(url_for("maChemTable"))

  else:
    return render_template("views/ma/ContainerInfoView.html",
                       config = config,
                       container = container,
                       chemical = chemical)