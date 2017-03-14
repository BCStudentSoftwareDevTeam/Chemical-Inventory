from application.models.util import *
from application.models.roomsModel import Rooms

class Storages(Model):
  sId           = PrimaryKeyField()
  roomId        = ForeignKeyField(Rooms) # When creating a container, select room first, then populate dropdown with all storages with matching roomId.
  oldPK         = IntegerField(null = True)
  name          = TextField() # Name of the specific storage unit ex: "Flammable Cabinet"
  # Booleans of true are what the storage is allowed to hold
  flammable     = BooleanField(default = False)
  healthHazard  = BooleanField(default = False)
  oxidizer      = BooleanField(default = False)
  orgAcid       = BooleanField(default = False)
  inorgAcid     = BooleanField(default = False)
  base          = BooleanField(default = False)
  peroxide      = BooleanField(default = False)
  pressure      = BooleanField(default = False)
  # refridgerated = BooleanField(default = False) # Do we need to check if a storage is refridgerated?

  class Meta:
    database = getDB("inventory", "dynamic")

def getStorages(room = None):
  if room == None:
    try:
      return Storages.select()
    except Exception as e:
      return e
  else:
    try:
      return Storages.select().where(Storages.roomId == room)
    except Exception as e:
      return e

def deleteStorage(storage):
  try:
    storage = Storages.get(Storages.sId == storage)
    storage.delete_instance(recursive=True)
  except Exception as e:
    return e
