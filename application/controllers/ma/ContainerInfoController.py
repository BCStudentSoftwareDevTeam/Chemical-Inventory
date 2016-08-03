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
@app.route('/ma/ContainerInfo/<chemId>/<barcodeId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maContainerInfo(chemId, barcodeId):
  chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  if chemical.remove == True:
    return redirect('ma/ChemTable')
  container = containersModel.Containers.get(containersModel.Containers.barcodeId == barcodeId)
  if container.disposalDate is not None:
    return redirect('ma/ChemTable')
  storageList = storagesModel.Storages.select()
  buildingList = buildingsModel.Buildings.select()
  histories = historiesModel.Histories.select().where(historiesModel.Histories.containerId == barcodeId)
  if request.method =="POST":
    data = request.form
    historiesModel.Histories(containerId = data['barcode'],
                            movedFrom = data['location'],
                            movedTo = data['storageId'],
                            pastQuantity = data['quantity'],
                            modDate = datetime.date.today()).save()
    cont = containersModel.Containers.get(barcodeId = barcodeId)
    cont.checkOutReason  = data['class']
    cont.checkedOut = True
    cont.forProf = data ['forProf']
    cont.storageId = data['storageId']
    cont.save()
    # add form data to container as checked out
    return redirect('/ma/ViewChemical/%s/%s/' %(chemical.name, chemId))
  else:
    return render_template("views/ma/ContainerInfoView.html",
                       config = config,
                       container = container,
                       chemical = chemical,
                       storageList = storageList,
                       buildingList = buildingList,
                       histories = histories)
                       
                       
@app.route('/sa/ContainerInfo/<chemId>/<barcodeId>/dispose/', methods = ['GET', 'POST'])
def maContainerDispose(chemId, barcodeId):
  chem = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  container = containersModel.Containers.get(containersModel.Containers.barcodeId == barcodeId)
  container.disposalDate = datetime.date.today()
  container.save()
  return redirect('/ma/ViewChemical/%s/%s/' %(chem.name, chem.chemId))