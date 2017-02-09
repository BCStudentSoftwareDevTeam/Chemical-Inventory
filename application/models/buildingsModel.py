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
  try:
    return Buildings.get(Buildings.bId == lId)
  except Exception as e:
    return e

def getBuildings():
  try:
    return Buildings.select()
  except Exception as e:
    return e
    
def editBuilding(data):
  try:
    building = Buildings.get(Buildings.bId == data['id']) #Get building to be edited
    building.name = data['name'] #Change all information to what was in the form
    building.numFloors = data['numFloors']
    building.address = data['address']
    building.save()
  except Exception as e:
    return e
    
def createBuilding(data):
  try:
    modelData, extraData = sortPost(data, Buildings)
    Buildings.create(**modelData)
  except Exception as e:
    return e
    
def deleteBuilding(bId):
  try:  
    building = getBuilding(bId)
    print bId
    building.delete_instance(recursive=True) # With recursive set to True, this will go through and delete the building and everything that is associated with it. ie: Floors, Rooms, and Storages
  except Exception as e:
    return e