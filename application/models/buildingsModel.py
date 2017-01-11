from application.models.util import *
from application.logic.sortPost import *

class Buildings (Model):
  bId        = PrimaryKeyField()
  name       = TextField() #Sans "Building"
  numFloors  = FloatField()
  address    = TextField()

  class Meta:
    database = getDB("inventory", "dynamic")

def getBuilding(lId):
  return Buildings.get(Buildings.bId == lId)

def getBuildings():
  return Buildings.select()
  
def editBuilding(data):
  building = Buildings.get(Buildings.bId == data['id']) #Get building to be edited
  building.name = data['name'] #Change all information to what was in the form
  building.numFloors = data['numFloors']
  building.address = data['address']
  building.save()
  
def createBuilding(data):
  modelData, extraData = sortPost(data, Buildings)
  Buildings.create(**modelData)
  
def deleteBuilding(bId):
  building = getBuilding(bId)
  print bId
  building.delete_instance(recursive=True) # With recursive set to True, this will go through and delete the building and everything that is associated with it. ie: Floors, Rooms, and Storages