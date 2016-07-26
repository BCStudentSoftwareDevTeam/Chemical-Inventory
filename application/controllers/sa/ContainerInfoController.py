from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *
import datetime

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
  histories = historiesModel.Histories.select().where(historiesModel.Histories.containerId == conId)
  if request.method =="POST":
    try:
      if request.form['dispose'] == "Dispose of this Container":
        container.disposalDate = datetime.now()
        container.save()
        return redirect(url_for("saChemTable"))
    except:
      data = request.form
      historiesModel.Histories(containerId = data['containerId'],
                               movedFrom = data['location'],
                               movedTo = data['storageId'],
                               pastUnit = data['unit'],
                               pastQuantity = data['quantity'],
                               modDate = datetime.now()).save()
      cont = containersModel.Containers.get(conId = conId)
      cont.checkOutReason  = data['class']
      cont.checkedOut = True
      cont.forProf = data ['forProf']
      cont.storageId = data['storageId']
      cont.save()
      # add form data to container as checked out
      return redirect('/sa/ViewChemical/%s/%s/' %(chemical.name, chemId))
  else:
    return render_template("views/sa/ContainerInfoView.html",
                       config = config,
                       container = container,
                       chemical = chemical,
                       storageList = storageList,
                       buildingList = buildingList,
                       histories = histories)
                       
@app.route('/sa/ContainerInfo/<chemId>/<conId>/dispose/', methods = ['GET', 'POST'])
def saContainerDispose(chemId, conId):
  chem = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  container = containersModel.Containers.get(containersModel.Containers.conId == conId)
  container.disposalDate = datetime.date.today()
  container.save()
  return redirect('/sa/ViewChemical/%s/%s/' %(chem.name, chem.chemId))