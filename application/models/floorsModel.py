from application.models.util import *
from application.models.buildingsModel import Buildings

class Floors (Model):
  fId          = PrimaryKeyField()
  buildid       = ForeignKeyField(Buildings)
  floornum      = TextField()
  storagelimits = TextField() # This needs to be populated with real storage limits

  class Meta:
    database = getDB("inventory")
