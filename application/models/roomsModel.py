from application.models.util import *
from application.models.floorsModel import Floors

class Rooms (Model):
  rId        = PrimaryKeyField()
  floorid    = ForeignKeyField(Floors)
  name       = TextField()

  class Meta:
    database = getDB("inventory")
