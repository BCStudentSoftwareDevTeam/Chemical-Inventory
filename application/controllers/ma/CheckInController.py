from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.models.storagesModel import *
from application.models.buildingsModel import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    jsonify, \
    url_for

# PURPOSE: CheckIn a container
@app.route('/ma/CheckIn/', methods = ['GET', 'POST'])
@require_role('admin')
def maCheckIn():
    storageList = Storages.select()
    buildingList = Buildings.select()
    if request.method == "POST":
        print request.method
        data = request.form
        cont = Containers.get(Containers.barcodeId == data['barcodeId'])
        cont.storageId = data['storageId']
        cont.currentQuantity = data['currentQuantity']
        cont.currentQuantityUnit = data['currentQuantityUnit']
        cont.checkedOut = False
        cont.checkOutReason =''
        cont.forProf = ''
        cont.checkedOutBy = ''
        print cont.checkedOut
        cont.save()
    return render_template("views/ma/CheckInView.html",
                           config = config,
                           contConfig = contConfig,
                           checkInConfig = checkInConfig,
                           container = None, #container = None is needed as a placeholder for the page before the barcode is entered.
                           buildingList = buildingList,
                           storageList = storageList,
                           checkOutConfig = checkOutConfig)

@app.route('/checkInData/', methods = ['GET']) #Called by AJAX from getData()
def checkInData():
    try:
        barId = request.args.get('barId') #Gets the variable that was sent via the AJAX call
        container = Containers.select().where(Containers.barcodeId == barId).dicts().get() #Get a dictionary of the container with matching barcode
        chemical = Chemicals.get(Chemicals.chemId == container['chemId']).name #Get the name of the chemical that this container refers to
        storage = Storages.get(Storages.sId == container['storageId']) #Get the storageId that this container refers to
        if storage.name != storage.roomId.name: #If the storage name is not the same as it's room name, show the building, room, and storage names
            location = storage.roomId.floorId.buildId.name + " Building, Room: " + storage.roomId.name + " (" + storage.name + ")"
        else: #If the storage name is the same as it's room name, only show building and roomm names
            location = storage.roomId.floorId.buildId.name + " Building, Room: " + storage.roomId.name
        if chemical is not None:
            return jsonify({'status':'OK', 'chemName' : chemical, 'storage' : location, 'quantity' : container['currentQuantity'], 'unit' : container['currentQuantityUnit']})
            #Return all data as a JSON object
    except:
        return jsonify({'status':'Error: There are no containers with that barcode in the system.'})