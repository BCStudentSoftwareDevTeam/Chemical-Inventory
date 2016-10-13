from application.models.util import *
from application.models.buildingsModel import Buildings

class Floors (Model):
  fId           = PrimaryKeyField()
  buildId       = ForeignKeyField(Buildings)
  name          = TextField()
  storageLimits = TextField(null = True) # This is additional functionality that does not need to be in the initial system

  class Meta:
    database = getDB("inventory", "dynamic")
