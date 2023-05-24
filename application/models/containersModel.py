from collections import defaultdict
import datetime

from peewee import *

from application.models import BaseModel
from application.models.util import *
from application.models.chemicalsModel import Chemicals
from application.models.storagesModel import Storages
from application.models.roomsModel import *
from application.models.roomsModel import Rooms
from application.models.storagesModel import Storages
from application.models.floorsModel import Floors
from application.models.buildingsModel import Buildings


class Containers (BaseModel):
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
  waste              = BooleanField(default = False) # If the container is in waste
  removalDate        = DateTimeField(null = True) # This will be for when waste is disposed
  peroxideCheckDate  = DateTimeField(null = True)


def getContainer(barcode):
  """Returns a Containers object with the given barcode"""
  try:
    return Containers.get((Containers.barcodeId == barcode)|(Containers.barcodeId == str(barcode).upper()))
  except:
    return False

def addContainer(data, user):
    """Used to add a new container

    Args:
        data (dict): From data input by user
        user (str): User creating container
    Returns:
        Array containing status details (Bool, Str, Str, Object_Created)
        """
    try:
        modelData, extraData = sortPost(data, Containers)
        cont = Containers.create(**modelData)
        application.models.historiesModel.updateHistory(cont, "Created", data['storageId'], user)
        return (True, "Container Created Successfully!", "list-group-item list-group-item-success", cont)
    except Exception as e:
        print(e)
        return (False, "Container Could Not Be Created!", "list-group-item list-group-item-danger", None)
    return Containers.get(Containers.barcodeId == barcode)

def changeLocation(cont, status, data, user):
  """Used to check containers in and out

  Args:
      container (Containers): the container to be changed
      status (bool): True if container is being checked out, False if checked in
      data (dict): Form data from user.
  Returns:
      Nothing
  """ #should return something for unit testing later
  print(data)
  if status: # True if checking out
    try:
      cont.storageId = data['storageId']
      cont.checkedOut = status
      cont.checkOutReason = data['forClass']
      cont.forProf = data['forProf']
      cont.checkedOutBy = user
      cont.save()
    except Exception as e:
      return e
  else: # Checking in
    try:
      cont.storageId = data['storageId']
      cont.currentQuantity = data['currentQuantity']
      cont.currentQuantityUnit = data['currentQuantityUnit']
      cont.checkedOut = status
      cont.checkOutReason = ''
      cont.forProf = ''
      cont.checkedOutBy = ''
      cont.save()
    except Exception as e:
      return e

def getChemicalContainers():
    """
        Returns a dictionary with keys of every chemical name referencing a list of available containers for checkout
    """
    query = (Chemicals.select(Chemicals,Containers)
                      .join(Containers, JOIN.LEFT_OUTER, on=(Containers.chemId_id==Chemicals.chemId), attr='container')
                      .where(Containers.disposalDate == None, Chemicals.remove == False)
                      .order_by(Chemicals.name))

    chemDict = defaultdict(list)
    for chem in query:
        chemDict[chem.name] = chemDict[chem.name] + ([chem.container] if hasattr(chem,'container') else [])

    return chemDict
    
def getContainers(storage):
  try:
    Containers.get(Containers.storageId == storage,
                   Containers.disposalDate == None)
  except Exception as e:
    return False


def disposeContainer(bId):
    try:
        cont = getContainer(bId)
        cont.disposalDate = datetime.date.today()
        cont.save()
        return (True, "Container "+ bId +" was removed successfully!", "list-group-item list-group-item-success")
    except Exception as e:
        return (False, "Container "+ bId +" was could not be removed!", "list-group-item list-group-item-danger")

def getAllDataAboutContainers():
    conts = (Containers.select(Containers,Chemicals,Storages,Rooms,Floors,Buildings)
                .join(Chemicals).switch(Containers)
                .join(Storages)
                .join(Rooms)
                .join(Floors)
                .join(Buildings))
    return list(conts)


from application import admin
from flask_admin.contrib.peewee import ModelView
admin.add_view(ModelView(Containers))

