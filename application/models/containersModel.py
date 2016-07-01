from application.models.util import *
from application.models.chemicalsModel import Chemicals
from application.models.storagesModel import Storages
import datetime

class Containers (Model):
  conId          = PrimaryKeyField()
   ##Foreign Keys
  chemId             = ForeignKeyField(Chemicals, related_name = 'chemical')
  storageId          = ForeignKeyField(Storages, related_name = 'storage')
  ##
  barcodeId          = CharField(null = False)
  #res_u_name         = ForeignKeyField(User, related_name = 'responsible')
  currentQuantityUnit= TextField() # units of chemical
  currentQuantity    = FloatField()# amount of chemical currently in container?
  receiveDate        = DateTimeField(default = datetime.datetime.now)
  disposalDate       = DateTimeField(null = True) # needed when container is empty??? To avoid deleting anything?
  conType            = CharField(default = "")
  manufacturer       = CharField(null = True)
  capacityUnit       = CharField(default = "") # units container is initially measured in
  capacity           = FloatField(null = False)# amount of units that the container can hold
  checkedOut         = BooleanField(default = False)
  forClass           = CharField(null = True)
  forProf            = CharField(null = True)
  checkedOutBy       = CharField(null = True)

  class Meta:
    database = getDB("inventory")
