from application.models.util import *
from application.models.buildingsModel import Buildings
from application.logic.sortPost import *

class Floors (Model):
  fId           = PrimaryKeyField()
  buildId       = ForeignKeyField(Buildings)
  name          = TextField()
  storageLimits = TextField(null = True) # This is additional functionality that does not need to be in the initial system

  class Meta:
    database = getDB("inventory", "dynamic")

def editFloor(data):
  floor = Floors.get(Floors.fId == data['id']) #Get floor to be edited and change all information to what was in form
  floor.name = data['name']
  floor.storageLimits = data['storageLimits']
  floor.save()
  
def createFloor(data):
  modelData, extraData = sortPost(data, Floors)
  Floors.create(**modelData)
  
def getFloors(building):
  return Floors.select().where(Floors.buildId == building)
  
def deleteFloor(building):
  Floors.get(Floors.fId == building)
  floor.delete_instance(recursive=True)