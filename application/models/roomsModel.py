from application.models.util import *
from application.models.floorsModel import Floors

class Rooms (Model):
  rId        = PrimaryKeyField()
  floorId    = ForeignKeyField(Floors, related_name = "floor")
  name       = TextField() #Room number. It is a text field to account for rooms like '13c' 

  class Meta:
    database = getDB("inventory", "dynamic")
