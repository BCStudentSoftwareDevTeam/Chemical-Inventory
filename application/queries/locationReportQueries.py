from application.models.chemicalsModel import *
from application.models.containersModel import Containers
from application.models.roomsModel import Rooms
from application.models.storagesModel import Storages
from application.models.floorsModel import Floors
from application.models.buildingsModel import Buildings
from application.models.buildingsModel import *
from application.models.historiesModel import *

def getChemInLoc(loc_data):
    ##Returns all containers, chem in Storages and rooms and floors in build
    conditionals = {"Building":"Buildings.bId == loc_data['Building']", "Floor":"Floors.fId == loc_data['Floor']", "Room":"Rooms.rId == loc_data['Room']", "Storage":"Storages.sId == loc_data['Storage']"}
    if loc_data["Building"] != "*":
        wheres = eval(conditionals["Building"])
        for value in loc_data:
            if value == "Building":
                pass
            elif loc_data[value] != "*":
                wheres &= eval(conditionals[value])
    else:
        wheres = Buildings.name == Buildings.name
    conts = (Containers.select() \
                .join(Storages, on = (Containers.storageId == Storages.sId)) \
                .join(Rooms, on = (Rooms.rId == Storages.roomId)) \
                .join(Floors, on = (Floors.fId == Rooms.floorId)) \
                .join(Buildings, on = (Buildings.bId == Floors.buildId)) \
                .where(wheres)\
                .switch(Containers))
    return conts

def getChemInStor(s_id):
    ##Done cont.storageId.roomId.floorId.buildId.name
    conts = (Containers.select() \
                .where(Containers.storageId == s_id))
    return conts

def getChemInRoom(r_id):
    ##Done
    ##Return all chemicals in Room
    conts = (Containers.select() \
                .join(Storages, on = (Containers.storageId == Storages.sId)) \
                .join(Rooms, on = (Rooms.rId == Storages.roomId)) \
                .where(Rooms.rId == r_id)
                .switch(Containers))
    return conts

def getChemInFloor(f_id):
    ##Done
    ##Return all containers, chem, in Storages and rooms on Floor
    conts = (Containers.select() \
                .join(Storages, on = (Containers.storageId == Storages.sId)) \
                .join(Rooms, on = (Rooms.rId == Storages.roomId)) \
                .join(Floors, on = (Floors.fId == Rooms.floorId)) \
                .where(Floors.fId == f_id) \
                .switch(Containers))
    return conts

def getChemInBuild(b_id):
    ##Returns all containers, chem in Storages and rooms and floors in build
    conts = (Containers.select() \
                .join(Storages, on = (Containers.storageId == Storages.sId)) \
                .join(Rooms, on = (Rooms.rId == Storages.roomId)) \
                .join(Floors, on = (Floors.fId == Rooms.floorId)) \
                .join(Buildings, on = (Buildings.bId == Floors.buildId)) \
                .where(Buildings.bId == b_id) \
                .switch(Containers))
    return conts

def getIAFlamLiquids():
    allIAFlam = (Containers.select() \
                    .join(Chemicals, on = (Containers.chemId == Chemicals.chemId)) \
                    .where((Chemicals.flashPoint < 73) & (Chemicals.boilPoint < 100))) \
                    .switch(Containers)
    return allIAFlam

