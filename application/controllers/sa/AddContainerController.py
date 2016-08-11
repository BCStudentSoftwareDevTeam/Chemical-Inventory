from application import app
from application.models.containersModel import *
from application.models.roomsModel import *
from application.models.storagesModel import *
from application.models.buildingsModel import *
from application.models.historiesModel import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    flash, \
    url_for

# PURPOSE: Add Container for a certain chemical
@app.route('/sa/AddContainer/<chemId>/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
def saAddContainer(chemId):
  chemInfo = Chemicals.get(Chemicals.chemId == chemId)
  storageList = Storages.select().order_by(Storages.roomId)
  buildingList = Buildings.select()
  if request.method == "POST":
    try: #If a form was posted, try to create a new container with info from form
      data = request.form
      modelData, extraData = sortPost(data, Containers)
      Containers.create(**modelData)
      Histories.create(movedTo = modelData['storageId'],
                 containerId = modelData['barcodeId'], 
                 modUser = extraData['user'], 
                 pastQuantity = "%s %s" %(modelData['currentQuantity'], modelData['currentQuantityUnit']))
      flash("Container added successfully") #Flash a success message
    except:
      flash("Container could not be added") #If there was an error, flash an error message
  lastCont = Containers.select().order_by(-Containers.barcodeId).get().barcodeId # Gets the last entered container. Used for creating the next barcode
  #lastCont needs to be assigned after any potential updates to the last barcode, and before render_template
  return render_template("views/sa/AddContainerView.html",
                         config = config,
                         contConfig = contConfig,
                         chemInfo = chemInfo,
                         storageList = storageList,
                         buildingList = buildingList,
                         lastCont = lastCont)