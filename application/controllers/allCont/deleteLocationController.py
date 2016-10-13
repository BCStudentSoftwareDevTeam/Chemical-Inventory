from application import app
from application.models.buildingsModel import Buildings
from application.models.floorsModel import Floors
from application.models.roomsModel import Rooms
from application.models.storagesModel import Storages
from application.models.containersModel import Containers
from application.models.util import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser
from application.logic.sortPost import *

from flask import \
    render_template, \
    redirect, \
    request, \
    flash, \
    url_for, \
    abort

@app.route('/delete/<location>/<lId>/', methods = ['GET', 'POST']) #Called from delete location modals
def maDelete(location, lId):
    auth = AuthorizedUser()
    user = auth.getUser()
    userLevel = auth.userLevel()
    if userLevel == -1 or user == -1:
        abort(403)
    print user.username, userLevel
  
    if userLevel == "admin":
        state = 0
        if request.method == "GET": #Calls delete queries based on what type of location is being deleted.
            if location == "Building":
                floors = Floors.select().where(Floors.buildId == lId) #All floors of the current building
                for floor in floors:
                    rooms = Rooms.select().where(Rooms.floorId == floor) #All rooms of current floor
                    for room in rooms:
                        storages = Storages.select().where(Storages.roomId == room) #All storage locations of current room
                        for storage in storages:
                            try:
                                Containers.get(Containers.storageId == storage, #Try to get any containers associated with current storage location
                                               Containers.disposalDate == None)
                                state = 1
                            except:
                                pass
                if state != 1:
                    building = Buildings.get(Buildings.bId == lId)
                    building.delete_instance(recursive=True) # With recursive set to True, this will go through and delete the building and everything that is associated with it. ie: Floors, Rooms, and Storages
                else:
                    flash("This building could not be deleted, as there are 1 or more containers still assigned to it.")
            elif location == "Floor":
                rooms = Rooms.select().where(Rooms.floorId == lId)
                for room in rooms:
                    storages = Storages.select().where(Storages.roomId == room)
                    for storage in storages:
                        try:
                            Containers.get(Containers.disposalDate == None,
                                           Containers.storageId == storage)
                            state = 1
                        except:
                            pass
                if state != 1:
                    floor = Floors.get(Floors.fId == lId)
                    floor.delete_instance(recursive=True)
                else:
                    flash("This floor could not be deleted, as there are 1 or more containers still assigned to it.")
            elif location == "Room":
                storages = Storages.select().where(Storages.roomId == lId)
                for storage in storages:
                    try:
                        Containers.get(Containers.disposalDate == None,
                                       Containers.storageId == storage)
                        state = 1
                    except:
                        pass
                if state != 1:
                    room = Rooms.get(Rooms.rId == lId)
                    room.delete_instance(recursive=True)
                else:
                    flash("This room could not be deleted, as there are 1 or more containers still assigned to it.")
            elif location == "Storage":
                try:
                    Containers.get(Containers.disposalDate == None,
                                   Containers.storageId == lId)
                    state = 1
                except:
                    pass
                if state != 1:
                    storage = Storages.get(Storages.sId == lId)
                    storage.delete_instance(recursive=True)
                else:
                    flash("This storage location could not be deleted, as there are 1 or more containers still assigned to it.")
        return redirect("/Home/") #need some js to handle this and edit in order to reload the page on the location tab
    else:
        abort(403)