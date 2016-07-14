# WARNING
# This script deletes the database file and configures empty
# tables for the models defined in the models module.
from application.models import classes
from application.models import *
from application.config import *
from datetime import date

def init_db ():
  # First, we create the databases.
  for database in config.databases:
    filename = config.databases[database].filename
    
    """Initializes the database."""
    # Remove the DB
    if os.path.isfile(filename):
      os.remove(filename)

    # Create an empty DB file
    open(filename, 'a').close()

  # Now, go through the modules we've discovered in the models directory.
  # Create tables for each model.
  for c in classes:
    c.create_table(True)
    

  print 'Initialized the database.'
  
  building = buildingsModel.Buildings(
    name = "Science",
    numFloors = "4.0",
    address = "101 Something Street").save()
  print "Building 1 saved"

  building2 = buildingsModel.Buildings(
    name = "The House",
    numFloors = "2.0",
    address = "Townsville USA").save()
  print "Building 2 saved"
  
  floorsModel.Floors(
    buildId = 1,
    floorNum = '1',
    storageLimits = "None").save()
  
  floorsModel.Floors(
    buildId = 1,
    floorNum = '2',
    storageLimits = "None").save()
    
  floorsModel.Floors(
    buildId = 1,
    floorNum = '3',
    storageLimits = "None").save()
  
  floorsModel.Floors(
    buildId = 1,
    floorNum = '4',
    storageLimits = "None").save()  

  floorsModel.Floors(
    buildId = 2,
    floorNum = '2',
    storageLimits = "None").save()

  floorsModel.Floors(
    buildId = 2,
    floorNum = '1',
    storageLimits = "None").save()
    
  print "All Floors Saved."
  
  roomsModel.Rooms(
    floorId = 1,
    name = "13b").save()

  roomsModel.Rooms(
    floorId = 1,
    name = "13c").save()
    
  roomsModel.Rooms(
    floorId = 2,
    name = "233").save()
    
  roomsModel.Rooms(
    floorId = 2,
    name = "200").save()

  roomsModel.Rooms(
    floorId = 4,
    name = "404").save()

  roomsModel.Rooms(
    floorId = 4,
    name = "420").save()

  roomsModel.Rooms(
    floorId = 5,
    name = "B07").save()

  roomsModel.Rooms(
    floorId = 5,
    name = "B11").save()

  roomsModel.Rooms(
    floorId = 6,
    name = "110").save()

  roomsModel.Rooms(
    floorId = 6,
    name = "Professor Utonium's Lab").save()
  print "All Rooms saved"
  
  storagesModel.Storages(
    roomId = 10,
    name = "Professor Utonium's Lab",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
    
  storagesModel.Storages(
    roomId = 3,
    name = "233",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
  
  storagesModel.Storages(
    roomId = 2,
    name = "Flammable Cabinet",
    flammable = True).save()
    
  storagesModel.Storages(
    roomId = 2,
    name = "Health Hazard Shelf",
    healthHazard = True).save()
    
  print "Storages Saved"
  
  chemicalsModel.Chemicals(
    name = "Acetone",
    casNum = "89-032-5324",
    primaryHazard = "Flammable",
    formula = "AcEtoNE",
    state = "Liquid",
    structure = "Inorganic",
    sdsLink = "https://www.link.com/Acetone",
    flashPoint = 999,
    boilPoint = 888,
    storageTemp = 69,
    healthHazard = "1",
    flammable = "4",
    reactive = "2").save()
    
  chemicalsModel.Chemicals(
    name = "Chemical X",
    casNum = "59-874-9721",
    primaryHazard = "Organic Health Hazard",
    formula = "ChEmIcaLX",
    state = "Liquid",
    structure = "Organic",
    sdsLink = "https://www.link.com/ChemicalX",
    flashPoint = 999,
    boilPoint = 888,
    storageTemp = 69,
    healthHazard = "4",
    flammable = "1",
    reactive = "0").save()
    
  containersModel.Containers(
    chemId = 1,
    storageId = 2,
    barcodeId = "16070000",
    currentQuantityUnit = "ounce (oz)",
    currentQuantity = 20,
    recieveDate = date.today(),
    conType = "bottle",
    manufacturer = "Sigma Aldrich",
    capacityUnit = "ounce (oz)",
    capacity = 20).save()
  
  containersModel.Containers(
    chemId = 2,
    storageId = 1,
    barcodeId = "16070001",
    currentQuantityUnit = "ounce (oz)",
    currentQuantity = 20,
    recieveDate = date.today(),
    conType = "bottle",
    manufacturer = "Sigma Aldrich",
    capacityUnit = "ounce (oz)",
    capacity = 20,
    checkedOut = True,
    forClass = "I think you get the reference",
    forProf = "Professor Utonium",
    checkedOutBy = "UtoniumP").save()
  
if __name__ == "__main__":
  init_db()
