from application.models.util import *
from application.models.buildingsModel import Buildings
from application.logic.sortPost import *

class Floors (Model):
  fId           = PrimaryKeyField()
  buildId       = ForeignKeyField(Buildings)
  name          = TextField()
  level         = IntegerField(null=False) #Level is for reporting

  class Meta:
    database = getDB("inventory", "dynamic")

def editFloor(data):
  try:
    floor = Floors.get(Floors.fId == data['id']) #Get floor to be edited and change all information to what was in form
    floor.name = data['name']
    floor.save()
    return(True, floor.name + " was Successfully Edited", "list-group-item list-group-item-success", floor)
  except Exception as e:
    return(False, floor.name + " Could Not Be Added to System", "list-group-item list-group-item-danger", floor)

def createFloor(data):
  try:
    print data
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
