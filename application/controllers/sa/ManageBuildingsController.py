from application import app
from application.models.buildingsModel import Buildings
from application.models.floorsModel import Floors
from application.models.roomsModel import Rooms
from application.models.storagesModel import Storages
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Edit, delete, and add buildings
@app.route('/sa/ManageBuildings/', methods = ['GET', 'POST'])
@require_role('admin')
def saManageBuildings():
    buildings = Buildings.select()
    floors = Floors.select()
    rooms = Rooms.select().order_by(+Rooms.name)
    storages = Storages.select()
    if request.method == "GET":
        return render_template("views/sa/ManageBuildingsView.html",
                               config = config,
                               locationConfig = locationConfig,
                               buildings = buildings,
                               floors = floors,
                               rooms = rooms,
                               storages = storages)
    data = request.form
    if data['location'] == "Building":
        building = Buildings.get(Buildings.bId == data['id'])
        building.name = data['name']
        building.numFloors = data['numFloors']
        building.address = data['address']
        building.save()
        return render_template("views/sa/ManageBuildingsView.html",
                               config = config,
                               locationConfig = locationConfig,
                               buildings = buildings,
                               floors = floors,
                               rooms = rooms,
                               storages = storages)
    elif data['location'] == "Floor":
        floor = Floors.get(Floors.fId == data['id'])
        floor.name = data['name']
        floor.storageLimits = data['storageLimits']
        floor.save()
        return render_template("views/sa/ManageBuildingsView.html",
                               config = config,
                               locationConfig = locationConfig,
                               buildings = buildings,
                               floors = floors,
                               rooms = rooms,
                               storages = storages)
    elif data['location'] == "Room":
        room = Rooms.get(Rooms.rId == data['id'])
        room.name = data['name']
        room.save()
        return render_template("views/ma/ManageBuildingsView.html",
                               config = config,
                               locationConfig = locationConfig,
                               buildings = buildings,
                               floors = floors,
                               rooms = rooms,
                               storages = storages)
    elif data['location'] == "Storage":
        storage = Storages.get(Storages.sId == data['id'])
        storage.name = data['name']
        storage.save()
        return render_template("views/sa/ManageBuildingsView.html",
                               config = config,
                               locationConfig = locationConfig,
                               buildings = buildings,
                               floors = floors,
                               rooms = rooms,
                               storages = storages)