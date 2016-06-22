from application.models.util import *

class Buildings (Model):
  bId        = PrimaryKeyField()
  name       = TextField()
  numfloors  = FloatField()
  address    = TextField()

  class Meta:
    database = getDB("inventory")
