from application.models.util import *
from application.models.chemicalsModel import Chemicals
from application.models.storagesModel import Storages
from application.models.roomsModel import *
import datetime

class Containers (Model):
  conId              = PrimaryKeyField()
  ##Foreign Keys
  chemId             = ForeignKeyField(Chemicals, related_name = 'chemical')
  storageId          = ForeignKeyField(Storages, related_name = 'storage')
  ##
  barcodeId          = CharField(null = False, unique = True)
  currentQuantityUnit= TextField() # units of chemical
  currentQuantity    = FloatField()# amount of chemical currently in container
  receiveDate        = DateTimeField(default = datetime.datetime.now)
  disposalDate       = DateTimeField(null = True)
  conType            = CharField(default = "")
  manufacturer       = CharField(null = True)
  capacityUnit       = CharField(default = "") # units container is initially measured in
  capacity           = FloatField(null = False)# amount of units that the container can hold
  checkedOut         = BooleanField(default = False) # set to True upon checkout
  checkOutReason     = CharField(null = True)
  forProf            = CharField(null = True)
  checkedOutBy       = CharField(null = True) # Will be filled in with users username upon checkout
  migrated           = IntegerField(null = True) # If the container was migrated from CISPro

  class Meta:
    database = getDB("inventory", "dynamic")

def getContainer(barcode):
  """Returns a Containers object with the given barcode"""
  return Containers.get(Containers.barcodeId == barcode)
  
def changeLocation(cont, status, data):
  """Used to check containers in and out
  
  Args:
      container (Containers): the container to be changed
      status (bool): True if container is being checked out, False if checked in
      data (dict): Form data from user.
  Returns:
      Nothing
  """ #should return something for unit testing later
  if status: # True if checking out
    cont.storageId = data['storageId']
    cont.checkedOut = status
    cont.checkOutReason = data['forClass']
    cont.forProf = data['forProf']
    cont.checkedOutBy = data['user']
    cont.save()
  else: # Checking in
    cont.storageId = data['storageId']
    cont.currentQuantity = data['currentQuantity']
    cont.currentQuantityUnit = data['currentQuantityUnit']
    cont.checkedOut = status
    cont.checkOutReason = ''
    cont.forProf = ''
    cont.checkedOutBy = ''
    cont.save()
    
def contCount(chemicals):
  """Gets a count of how many containers are currently checked in and not disposed of for each chemical
  
  Args:
      chemicals (list): a list of all chemicals in the database
  Returns:
      dict: a dictionary with keys of every chemical name, and values of how many containers are available for checkout
  """
  contDict = {} #Set up a dictionary for all containers
  for chemical in chemicals: #For each chemical
    contDict[chemical.name] = ((((Chemicals
                              .select())
                              .join(Containers))
                              .where(
                                (Containers.disposalDate == None) &
                                (Containers.chemId == chemical.chemId) &
                                (Chemicals.remove == False))
                              .count()))
  return contDict

def getContainers(storage):
  Containers.get(Containers.storageId == storage,
                 Containers.disposalDate == None)