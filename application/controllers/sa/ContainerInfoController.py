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
@app.route('/sa/ContainerInfo/<chemId>/<conId>/', methods = ['GET', 'POST'])
@require_role('admin')
def saContainerInfo(chemId, conId):
  chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  container = containersModel.Containers.get(containersModel.Containers.conId == conId)
  storageList = storagesModel.Storages.select()
  buildingList = buildingsModel.Buildings.select()
  if request.method =="POST":
    try:
      if request.form['dispose'] == "Dispose of this Container":
        container.disposalDate = datetime.now()
        container.save()
        return redirect(url_for("saChemTable"))
    except:
      # add form data to container as checked out
      return render_template("views/sa/ContainerInfoView.html",
                             config = config,
                             container = container,
                             chemical = chemical,
                             storageList = storageList,
                             buildingList = buildingList)
  else:
    return render_template("views/sa/ContainerInfoView.html",
                       config = config,
                       container = container,
                       chemical = chemical,
                       storageList = storageList,
                       buildingList = buildingList)