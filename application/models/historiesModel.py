from application.models.util import *
from application.models.storagesModel import Storages
from application.models.containersModel import Containers
import datetime

class Histories (Model):
  hId          = PrimaryKeyField()
  ##Foreign Keys
  movedFrom     = ForeignKeyField(Storages, related_name="movedFrom")
  movedTo       = ForeignKeyField(Storages, related_name="movedTo")
  containerId   = ForeignKeyField(Containers, related_name = "containers")
  ##
  pastUnit      = TextField() # Container.currentUnit unit last entered.
  pastQuantity  = FloatField()# Container.currentQuantity amount of chemical last in the container
  modDate       = DateTimeField(default = datetime.datetime.now)

  class Meta:
    database = getDB("inventory")
