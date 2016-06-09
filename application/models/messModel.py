from application.models.util import *

class Mess (Model):
  mid     = PrimaryKeyField()
  id      = TextField()
  data    = TextField()
  size    = IntegerField()

  class Meta:
    database = getDB("mess")
