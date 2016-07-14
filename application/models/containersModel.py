from application.models.util import *
from application.models.chemicalsModel import Chemicals
from application.models.storagesModel import Storages
from application.models.roomsModel import *
import datetime

class Containers (Model):
  conId          = PrimaryKeyField()
  ##Foreign Keys
  chemId             = ForeignKeyField(Chemicals, related_name = 'chemical')
  storageId          = ForeignKeyField(Storages, related_name = 'storage')
  ##
  barcodeId          = CharField(null = False)
  currentQuantityUnit= TextField() # units of chemical
  currentQuantity    = FloatField()# amount of chemical currently in container
  receiveDate        = DateTimeField(default = datetime.datetime.now)
  disposalDate       = DateTimeField(null = True)
  conType            = CharField(default = "")
  manufacturer       = CharField(null = True) # Why is manufacturer allowed to be null?
  capacityUnit       = CharField(default = "") # units container is initially measured in
  capacity           = FloatField(null = False)# amount of units that the container can hold
  checkedOut         = BooleanField(default = False) # set to True upon checkout
  forClass           = CharField(null = True) # Required field on checkout page
  forProf            = CharField(null = True) # Required field on checkout page
  checkedOutBy       = CharField(null = True) # Required field on checkout page

  class Meta:
    database = getDB("inventory")
