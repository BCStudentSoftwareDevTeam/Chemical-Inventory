from application.models.util import *

class Buildings (Model):
  bId        = PrimaryKeyField()
  name       = TextField() #Sans "Building"
  numFloors  = FloatField()
  address    = TextField()

  class Meta:
    database = getDB("inventory", "dynamic")
