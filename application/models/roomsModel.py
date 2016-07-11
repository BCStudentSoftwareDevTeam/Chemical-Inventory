from application.models.util import *
from application.models.floorsModel import Floors

class Rooms (Model):
  rId        = PrimaryKeyField()
  floorId    = ForeignKeyField(Floors, related_name = "floor")
  name       = TextField()

  class Meta:
    database = getDB("inventory")
