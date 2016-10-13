# WARNING
# This script deletes the database file and configures empty
# tables for the models defined in the models module.
from application.models import classes
from application.config import *
from application.models import *
import datetime
    
def init_db ():
  # First, we create the databases.
  for database in config.databases.dynamic:
    filename = config.databases.dynamic[database].filename
    
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
    name = "Danforth Industrial Arts",
    numFloors = "2.0",
    address = "By the big hole in the ground").save()
  print "Building 2 saved"
  
  floorsModel.Floors(
    buildId = 1,
    name = 'Basement',
    storageLimits = "None").save()
  
  floorsModel.Floors(
    buildId = 1,
    name = '2',
    storageLimits = "None").save()
    
  floorsModel.Floors(
    buildId = 1,
    name = '3',
    storageLimits = "None").save()
  
  floorsModel.Floors(
    buildId = 1,
    name = '4',
    storageLimits = "None").save()  

  floorsModel.Floors(
    buildId = 2,
    name = '1',
    storageLimits = "None").save()

  floorsModel.Floors(
    buildId = 2,
    name = '2',
    storageLimits = "None").save()
    
  print "All Floors Saved."
  
  roomsModel.Rooms( #1
    floorId = 1,
    name = "13b").save()

  roomsModel.Rooms( #2
    floorId = 1,
    name = "13c").save()
    
  roomsModel.Rooms( #3
    floorId = 2,
    name = "233").save()
    
  roomsModel.Rooms( #4
    floorId = 2,
    name = "200").save()
    
  roomsModel.Rooms( #5
    floorId = 3,
    name= "330").save()

  roomsModel.Rooms( #6
    floorId = 4,
    name = "404").save()

  roomsModel.Rooms( #7
    floorId = 4,
    name = "420").save()

  roomsModel.Rooms( #8
    floorId = 6,
    name = "B07").save()

  roomsModel.Rooms( #9
    floorId = 6,
    name = "B11").save()

  roomsModel.Rooms( #10
    floorId = 5,
    name = "110").save()

  roomsModel.Rooms( #11
    floorId = 5,
    name = "111").save()
  print "All Rooms saved"
  
  storagesModel.Storages(
    roomId = 1,
    name = "Health Hazard Shelf",
    healthHazard = True).save()  
    
  storagesModel.Storages(
    roomId = 2,
    name = "Flammable Cabinet",
    flammable = True).save()
    
  storagesModel.Storages(
    roomId = 2,
    name = "Health Hazard Shelf",
    healthHazard = True).save()
        
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
    roomId = 4,
    name = "200",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
    
  storagesModel.Storages(
    roomId = 5,
    name = "330",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
    
  storagesModel.Storages(
    roomId = 6,
    name = "404",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()

  storagesModel.Storages(
    roomId = 7,
    name = "420",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
    
  storagesModel.Storages(
    roomId = 8,
    name = "B07",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
    
  storagesModel.Storages(
    roomId = 9,
    name = "Organic Acid Shelf",
    orgAcid = True).save()
    
  storagesModel.Storages(
    roomId = 9,
    name = "Inorganic Acid Shelf",
    inorgAcid = True).save()
  
  storagesModel.Storages(
    roomId = 10,
    name = "110",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
    
  storagesModel.Storages(
    roomId = 11,
    name = "111",
    flammable = True,
    healthHazard = True,
    oxidizer = True,
    orgAcid = True,
    inorgAcid = True,
    base = True,
    peroxide = True,
    pressure = True).save()
    
  print "Storages Saved"
  
  chemicalsModel.Chemicals(
    name = "Acetone",
    casNum = "89-032-5324",
    primaryHazard = "Flammable",
    formula = "AcEtoNE",
    state = "Liquid",
    structure = "Inorganic",
    sdsLink = "https://msdsmanagement.msdsonline.com/af807f3c-b6be-4bd0-873b-f464c8378daa/ebinder/33233069/",
    description = "This is acetone... I don't know what it does or looks like",
    hmisHealth = "1",
    hmisFlammable = "4",
    hmisPhysical = "2",
    hmisPPE = "B",
    flashPoint = 999,
    boilPoint = 888,
    storageTemp = 69,
    flamePict = True,
    peroxideFormer = True,
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
    sdsLink = "https://msdsmanagement.msdsonline.com/af807f3c-b6be-4bd0-873b-f464c8378daa/ebinder/32357647/",
    description = "This is chemicalX... I don't know what it does or looks like",
    hmisHealth = "4",
    hmisFlammable = "1",
    hmisPhysical = "0",
    hmisPPE = "H",
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
    recieveDate = datetime.date.today(),
    conType = "bottle",
    manufacturer = "Sigma Aldrich",
    capacityUnit = "ounce (oz)",
    capacity = 20).save()
    
  containersModel.Containers(
    chemId = 1,
    storageId = 2,
    barcodeId = "16070001",
    currentQuantityUnit = "ounce (oz)",
    currentQuantity = 0,
    recieveDate = datetime.date.today(),
    conType = "bottle",
    manufacturer = "Sigma Aldrich",
    capacityUnit = "ounce (oz)",
    capacity = 20).save()
    
  containersModel.Containers(
    chemId = 1,
    storageId = 8,
    barcodeId = "16060003",
    currentQuantityUnit = "ounce (oz)",
    currentQuantity = 18.4,
    recieveDate = datetime.date.today(),
    conType = "bottle",
    manufacturer = "Sigma Aldrich",
    capacityUnit = "ounce (oz)",
    checkedOut = True,
    checkedOutBy = "Nick DeTore",
    forProf = "Scott Heggen",
    checkOutReason = "Ummmmm... I don't know.",
    capacity = 20).save()
  
  containersModel.Containers(
    chemId = 2,
    storageId = 11,
    barcodeId = "15080000",
    currentQuantityUnit = "ounce (oz)",
    currentQuantity = 17,
    recieveDate = datetime.date.today(),
    conType = "bottle",
    manufacturer = "Sigma Aldrich",
    capacityUnit = "ounce (oz)",
    capacity = 20,
    checkedOut = True,
    checkOutReason = "I think you get the reference",
    forProf = "Professor Utonium",
    checkedOutBy = "UtoniumP").save()    

  historiesModel.Histories(
    movedFrom = 5,
    movedTo = 8,
    modUser = "Nick DeTore",
    containerId = 16070000,
    action = "Created",
    pastQuantity = "20.0 ounce (oz)",
    modDate = "01/20/2012").save()
    
  historiesModel.Histories(
    movedFrom = 5,
    movedTo = 8,
    modUser = "Nick DeTore",
    containerId = 16070001,
    action = "Created",
    pastQuantity = "20.0 ounce (oz)",
    modDate = "01/20/2012").save()
    
  historiesModel.Histories(
    movedFrom = 5,
    movedTo = 8,
    modUser = "Nick DeTore",
    containerId = 16060003,
    action = "Created",
    pastQuantity = "20.0 ounce (oz)",
    modDate = "01/20/2012").save()
    
  historiesModel.Histories(
    movedFrom = 8,
    movedTo = 1,
    modUser = "Jesson Soto",
    containerId = 16060003,
    action = "Checked Out",
    pastQuantity = "20.0 ounce (oz)",
    modDate = "01/22/2012").save()   

  historiesModel.Histories(
    movedFrom = 8,
    movedTo = 1,
    modUser = "Jesson Soto",
    containerId = 15080000,
    action = "Created",
    pastQuantity = "20.0 ounce (oz)",
    modDate = "01/22/2012").save()   
    
  historiesModel.Histories(
    movedFrom = 8,
    movedTo = 1,
    modUser = "Jesson Soto",
    containerId = 15080000,
    action = "Checked Out",
    pastQuantity = "20.0 ounce (oz)",
    modDate = "01/22/2012").save()   

if __name__ == "__main__":
  init_db()
