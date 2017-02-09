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
  try:
    floor = Floors.get(Floors.fId == data['id']) #Get floor to be edited and change all information to what was in form
    floor.name = data['name']
    floor.storageLimits = data['storageLimits']
    floor.save()
  except Exception as e:
    return e

def createFloor(data):
  try:
    modelData, extraData = sortPost(data, Floors)
    Floors.create(**modelData)
  except Exception as e:
    return e
    
def getFloors(building):
  try:
    return Floors.select().where(Floors.buildId == building)
  except Exception as e:
    return e

def deleteFloor(building):
  try:
    Floors.get(Floors.fId == building)
    floor.delete_instance(recursive=True)
  except Exception as e:
    return e