from application import app
from application.models.containersModel import *
from application.models.roomsModel import *
from application.models.storagesModel import *
from application.models.buildingsModel import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    flash, \
    url_for

# PURPOSE: Add Container for a certain chemical
@app.route('/ma/AddContainer/<chemName>/<chemId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maAddContainer(chemName, chemId):
  chemInfo = Chemicals.get(Chemicals.chemId == chemId)
  storageList = Storages.select().order_by(Storages.roomId)
  buildingList = Buildings.select()
  lastCont = Containers.select().order_by(-Containers.barcodeId).get() # Gets the last entered container. Used for creating the next barcode
  
  if request.method == "GET":
      return render_template("views/ma/AddContainerView.html",
                             config = config,
                             contConfig = contConfig,
                             chemInfo = chemInfo,
                             storageList = storageList,
                             buildingList = buildingList,
                             lastCont = lastCont)
  try: #If a form was posted, try to create a new container with info from form
    data = request.form
    modelData, extraData = sortPost(data, Containers)
    Containers.create(**modelData)
    flash("Container added successfully") #Flash a success message
  except:
    flash("Container could not be added") #If there was an error, flash an error message
  return render_template("views/ma/AddContainerView.html",
                         config = config,
                         contConfig = contConfig,
                         chemInfo = chemInfo,
                         storageList = storageList,
                         buildingList = buildingList,
                         lastCont = lastCont)