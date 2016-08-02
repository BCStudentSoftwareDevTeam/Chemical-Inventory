from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.models.storagesModel import *
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

  if request.method == "GET":
    return render_template("views/ma/CheckInView.html",
                           config = config,
                           contConfig = contConfig,
                           checkInConfig = checkInConfig,
                           container = None)
  
@app.route('/checkInData/', methods = ['GET'])
def checkInData():
    barId = request.args.get('barId')
    container = Containers.select().where(Containers.barcodeId == barId).dicts().get()
    chemical = Chemicals.get(Chemicals.chemId == container['chemId']).name
    storage = Storages.get(Storages.sId == container['storageId'])
    if storage.name != storage.roomId.name:
        location = storage.roomId.floorId.buildId.name + " Building, Room: " + storage.roomId.name + " (" + storage.name + ")"
    else:
        location = storage.roomId.floorId.buildId.name + " Building, Room: " + storage.name
    return jsonify({'status':'OK', 'chemName' : chemical, 'storage' : location, 'quantity' : container['currentQuantity'], 'unit' : container['currentQuantityUnit']})