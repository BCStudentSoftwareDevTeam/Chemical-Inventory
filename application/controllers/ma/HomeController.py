from application import app
from application.models.buildingsModel import Buildings
from application.models.floorsModel import Floors
from application.models.roomsModel import Rooms
from application.models.storagesModel import Storages
from application.config import *
from application.logic.sortPost import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    redirect, \
    request, \
    url_for

####################################################
@app.route("/") # TAKE THIS OUT! JUST FOR TESTING ##
def homeRedr():
    return redirect('/ma/Home/')
####################################################
# PURPOSE: Edit, delete, and add buildings
@app.route('/ma/Home/', methods = ['GET', 'POST'])
@require_role('admin')
def adminHome():
    buildings = Buildings.select()
    floors = {}
    rooms = {}
    storages = {}
    if request.method == "POST":
        data = request.form #If a form is posted to the page
        if data['location'] == "Building": #If the form is editing a building
            if data['action'] == 'edit':
                building = Buildings.get(Buildings.bId == data['id']) #Get building to be edited
                building.name = data['name'] #Change all information to what was in the form
                building.numFloors = data['numFloors']
                building.address = data['address']
                building.save()
            elif data['action'] == 'add':
                modelData, extraData = sortPost(data, Buildings)
                Buildings.create(**modelData)
        elif data['location'] == "Floor": #If the form is editing a floor
            if data['action'] == 'edit':
                floor = Floors.get(Floors.fId == data['id']) #Get floor to be edited and change all information to what was in form
                floor.name = data['name']
                floor.storageLimits = data['storageLimits']
                floor.save()
            elif data['action'] == 'add':
                modelData, extraData = sortPost(data, Floors)
                Floors.create(**modelData)
        elif data['location'] == "Room": #If the form is editing a room
            if data['action'] == 'edit':
                room = Rooms.get(Rooms.rId == data['id']) #Get room to be edited and change all information to what was in form
                room.name = data['name']
                room.save()
            elif data['action'] == 'add':
                modelData, extraData = sortPost(data, Rooms)
                Rooms.create(**modelData)
        elif data['location'] == "Storage": #If the form is editing a storage
            if data['action'] == 'edit':
                storage = Storages.get(Storages.sId == data['id']) #Get storage location to be edited and change all information to what was in form
                for i in data:
                    setattr(storage, i, data[i])
                storage.save()
            elif data['action'] == 'add':
                modelData, extraData = sortPost(data, Storages)
                Storages.create(**modelData)
    for building in buildings: #Set floor dictionary with key of current building, and value of all floors that reference that building
        floors[building.bId] = Floors.select().where(Floors.buildId == building.bId)
        for floor in floors[building.bId]: #Set room dictionary with key of current floor, and value of all rooms that reference that floor
            rooms[floor.fId] = Rooms.select().where(Rooms.floorId == floor.fId).order_by(+Rooms.name)
            for room in rooms[floor.fId]: #Set storage dictionary with key of current room, and value of all storages that reference that room
                storages[room.rId] = Storages.select().where(Storages.roomId == room.rId)
    return render_template("views/ma/HomeView.html",
                           config = config,
                           locationConfig = locationConfig,
                           buildings = buildings,
                           floors = floors,
                           rooms = rooms,
                           storages = storages)
