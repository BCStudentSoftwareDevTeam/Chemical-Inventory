from application.models.util import *
from application.models.buildingsModel import Buildings

class Floors (Model):
  fId          = PrimaryKeyField()
  buildid       = ForeignKeyField(Buildings)
  floornum      = TextField()
  storagelimits = TextField() # This is additional functionality that does not need to be in the initial system

  class Meta:
    database = getDB("inventory")
