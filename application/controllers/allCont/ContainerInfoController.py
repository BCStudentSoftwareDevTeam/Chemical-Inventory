from application import app
from application.models import *
from application.models.containersModel import *
from application.models.historiesModel import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser
from application.logic.sortPost import *
import datetime

from flask import \
    render_template, \
    request, \
    redirect, \
    url_for, \
    abort

# PURPOSE: CheckOut a container
@app.route('/ContainerInfo/<chemId>/<barcodeId>/', methods = ['GET', 'POST'])
def maContainerInfo(chemId, barcodeId):
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  print user.username, userLevel

  if userLevel == "admin" or userLevel == "systemAdmin":
    chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
    if chemical.remove == True:
      return redirect('/ChemTable')
    container = containersModel.Containers.get(containersModel.Containers.barcodeId == barcodeId)
    if container.disposalDate is not None:
      return redirect('/ChemTable')
    storageList = storagesModel.Storages.select()
    buildingList = buildingsModel.Buildings.select()
    histories = historiesModel.Histories.select().where(historiesModel.Histories.containerId == container.conId)
    if request.method =="POST":
      data = request.form
      if data['formName'] == 'checkOutForm':
          print "Check Out Form"
          historiesModel.Histories(containerId = container.conId,
                                  barcodeId  = container.barcodeId,
                                  movedFrom = container.storageId_id,
                                  movedTo = data['storageId'],
                                  pastQuantity = str(container.currentQuantity) + str(container.currentQuantityUnit),
                                  modUser = user.username,
                                  action = "Checked Out",
                                  modDate = datetime.date.today()).save()
          cont = containersModel.Containers.get(barcodeId = barcodeId)
          cont.checkOutReason  = data['class']
          cont.checkedOut = True
          cont.checkedOutBy = user.username
          cont.forProf = data ['forProf']
          cont.storageId = data['storageId']
          cont.save()
          # add form data to container as checked out
          return redirect('/ViewChemical/%s/' %(chemId))
      else: #If it is checkIn
        try:
            data = request.form
            cont = Containers.get(Containers.barcodeId == data['barcodeId'])
            Histories.create(movedFrom = cont.storageId,
                           movedTo = data['storageId'],
                           containerId = cont.conId,
                           modUser = user.username,
                           action = "Checked In",
                           pastQuantity = "%s %s" %(cont.currentQuantity, cont.currentQuantityUnit))
            cont.storageId = data['storageId']
            cont.currentQuantity = data['currentQuantity']
            cont.currentQuantityUnit = data['currentQuantityUnit']
            cont.checkedOut = False
            cont.checkOutReason =''
            cont.forProf = ''
            cont.checkedOutBy = ''
            cont.save()
        except Exception as e:
            print data
            print e
        return redirect('/ViewChemical/%s/' %(chemId))
    else:
      return render_template("views/ContainerInfoView.html",
                         config = config,
                         contConfig = contConfig,
                         pageConfig = checkInConfig,
                         container = container,
                         chemical = chemical,
                         storageList = storageList,
                         buildingList = buildingList,
                         histories = histories,
                         authLevel = userLevel)
  else:
    abort(403)


@app.route('/ContainerInfo/<chemId>/<barcodeId>/dispose/', methods = ['GET', 'POST'])
def maContainerDispose(chemId, barcodeId):
  chem = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  container = containersModel.Containers.get(containersModel.Containers.barcodeId == barcodeId)
  container.disposalDate = datetime.date.today()
  container.save()
  return redirect('/ViewChemical/%s/' %(chem.chemId))
