from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.models.roomsModel import *
from application.models.storagesModel import *
from application.models.buildingsModel import *
from application.models.historiesModel import *
from application.config import *
from application.logic.validation import require_role
from urllib import *
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    redirect, \
    flash, \
    url_for

# PURPOSE: Shows specific chemical and all containers of said chemical.
@app.route('/ma/ViewChemical/<chemId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maViewChemical(chemId):
  chemInfo = Chemicals.get(Chemicals.chemId == chemId) #Get chemical by correct chemId
  chemDict = Chemicals.select().where(Chemicals.chemId == chemId).dicts().get() #Get chemical by correct chemId as a dictionary
  storageList = Storages.select().order_by(Storages.roomId)
  buildingList = Buildings.select()
  if chemInfo.remove == True: #If the chemical attribute, 'remove', was set to True, go back to the chemical table.
    return redirect('ma/ChemTable')
  if request.method == "POST": #If there was a form posted to this page
    data = request.form
    if data['formName'] == 'addChem':
      for i in data: #Loop through the keys in the form dictionary
        setattr(chemInfo, i, data[i]) #Set the attribute, 'i' (the current key in the form), of 'chemInfo' (the chemical) to the value of the current key in the form
      chemInfo.save()
    elif data["formName"] == "addCont":
      try: #If a form was posted, try to create a new container with info from form
        modelData, extraData = sortPost(data, Containers)
        cont = Containers.create(**modelData)
        Histories.create(movedTo = modelData['storageId'],
                        containerId = cont.barcodeId, 
                        modUser = extraData['user'],
                        action = "Created",
                        pastQuantity = "%s %s" %(modelData['currentQuantity'], modelData['currentQuantityUnit']))
        flash("Container added successfully") #Flash a success message
      except Exception as e:
        flash("Container could not be added") #If there was an error, flash an error message
  lastCont = Containers.select().order_by(-Containers.barcodeId).get().barcodeId # Gets the last entered container. Used for creating the next barcode
  #lastCont needs to be assigned after any potential updates to the last barcode, and before render_template
  containers = (((Containers
                .select())
                .join(Chemicals))
                .where(
                  (Containers.chemId == chemId) &
                  (Containers.disposalDate == None)
                ))
  #(Above) Get all containers of this chemical that haven't been disposed of
  return render_template("views/ma/ViewChemicalView.html",
                         config = config,
                         chemInfo = chemInfo,
                         containers = containers,
                         contConfig = contConfig,
                         chemConfig = chemConfig,
                         storageList = storageList,
                         buildingList = buildingList,
                         lastCont = lastCont,
                         authLevel = "admin")
                         
@app.route('/ma/ViewChemical/<chemId>/delete/', methods = ['GET','POST']) #When master admin clicks on delete chemical button. (button only show up when all containers of it have been disposed of)
def maDeleteChemical(chemId):
  chem = Chemicals.get(Chemicals.chemId == chemId) #Get chemical by correct chemId
  chem.deleteDate = datetime.date.today() #Set chemical's delete date to the current date
  chem.remove = True #Set chemical's remove attribute to true.
  chem.save() #We are not deleting the chemical because chemicals that are disposed still reference the chemical, and the containers are used for reports on disposal.
  return redirect('/ma/ChemTable')
