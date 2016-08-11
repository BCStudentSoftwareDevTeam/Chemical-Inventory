from application.models.util import *
from application.models.storagesModel import Storages
from application.models.containersModel import Containers
import datetime

class Histories (Model):
  hId          = PrimaryKeyField()
  ##Foreign Keys
  movedFrom     = ForeignKeyField(Storages, related_name="movedFrom", null = True)
  movedTo       = ForeignKeyField(Storages, related_name="movedTo")
  containerId   = ForeignKeyField(Containers, related_name = "containers")
  ##
  modUser       = TextField(null = True) # This should probably eventually be a foreign key to the users table.
  ##
  pastQuantity  = CharField()# This holds both the quantity and unit as a string. Since it won't be changed, the two fields could be combined
  modDate       = DateTimeField(default = datetime.datetime.now) #If a history instance is made, and the call doesn't specify the date, the default will take care of it

  class Meta:
    database = getDB("inventory")
