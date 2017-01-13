from application.models import classes
from application.config import *
from application.models import *
from application.models.staticModels.batchModel import *
from application.models.staticModels.mainModel import *
from application.models.staticModels.locatesModel import *
from application.models.chemicalsModel import *
from application.models.storagesModel import *
from application.models.historiesModel import *
from application.models.usersModel import *
import random
import datetime

def init_db():
    #Create the databases
    for database in config.databases.dynamic:
        filename = config.databases.dynamic[database].filename

        #Remove the DB
        if os.path.isfile(filename):
            os.remove(filename)

        #create an empty DB file
        open(filename, 'a').close()

    #Go through modules in models directory, and create a table for each one
    for c in classes:
        c.create_table(True)

    print 'Database Initialized'
    ####
    #Import MAINN table in CISPro into inventory.sqlite
    ####
    main_table = Main.select()
    for chem in  main_table:
        #Translate the form: int in CISPro -> string BCCIS
        state_map = {'0':"Solid", '1':"Liquid",'2':"Gas"}
        state = state_map[chem.State]

        #Translate the structure: int CISPro -> string BCCIS
        if chem.Organic == 1:
            struct = "Organic"
        elif chem.Inorganic == 1:
            struct = "Inorganic"
        else:
            struct = "Unknown"

        #Translate Hazards for icon fields: int CISPro -> bool BCCIS
        if chem.Hazardous == 1 or chem.Carcinogenic == 1:
            hhazard = True
        else:
            hhazard = False
        if state == 3:
            gascylinder = True
        else:
            gascylinder = False
        try:
            if (chem.ID2).upper == 'YELLOW':
                oxidizer = True
            else:
                oxidizer = False
        except:
            oxidizer = False

        #List of all possible Primary Hazards, one of these is randomly selected for the chem hazard. This is because of incosistant id3 data. ONLY FOR TESTING
        primaryHazard= ["Base", "Flammable", "Flammable Solid", "Health Hazard", "Inorganic Acid", "Organic Acid", "Oxidizer", "Reactive", "General Hazard"]

        #Checks if BoilingPoint or MolecularWeight are empty fields, so that Peewee doesn't default the value to 0.
        if chem.BoilingPoint == "":
            bPoint = None
        else:
            bPoint = chem.BoilingPoint
        if chem.molecularWeight == "":
            mWeight = None
        else:
            mWeight = chem.molecularWeight

        #Populates the Chemical modedl
        chemicalsModel.Chemicals(
            oldPK          = chem.NameSorted, #This keeps track of old primary key in CISPro so conts can relate back.
            name           = chem.NameRaw,
            casNum         = chem.casNo,
            primaryHazard  = primaryHazard[random.randrange(0, 9)],#chem.Id3 #This randomly selects pHaz
            formula        = chem.StructuralFormula,
            state          = state,
            structure      = struct,
            description    = chem.PhysicalDescription,
            healthHazard   = chem.Nfpa_Health,
            flammable      = chem.Nfpa_Flamable,
            reactive       = chem.Nfpa_Reactive,
            boilPoint      = bPoint,
            molecularWeight= mWeight,
            flamePict      = chem.Flamable,
            hhPict         = hhazard,
            gcPict         = gascylinder,
            corrosivePict  = chem.Corrosive,
            expPict        = chem.Explosive,
            oxidizerPict   = oxidizer).save()
        #print chem.NameRaw + " was added to the database"
    print "Chemicals were added to the database"

    ####
    #Makes one building that the one floor is put in
    ####
    buildingsModel.Buildings(
        name               = "Science Building",
        numFloors          = 12,
        address            = "101 Chestnut St. Berea, KY").save()
    print "Buildings were added to the database"

    ####
    #Makes one floor that the one room is put in
    ####
    floorsModel.Floors(
        buildId         = 1,
        name            = "First Floor").save()
    print "Floors were added to the database"

    ####
    #Makes a single room that all storages are put in
    ####
    roomsModel.Rooms(
            name    = "Super Room",
            floorId = 1).save()
    print "Rooms were added to the database"

    ####
    #Import LOCATES Table from CISPro into inventory.sqlite
    ###
    locates_table = Locates.select()
    for location in locates_table:
        storagesModel.Storages(
                oldPK      = location.Location,
                roomId    = 1,
                name       = location.NameSorted).save()
        #print location.NameSorted + " was added to STORAGES"
    print "Storages were added to the database"

    ####
    #Import BATCHES Table from CISPro into inventory.sqlite
    ####
    cont_table = Batch.select()
    for cont in cont_table:
        relChemId = Chemicals.select(Chemicals.chemId).where(Chemicals.oldPK == cont.NameRaw_id).get()
        relStorId = Storages.select(Storages.sId).where(Storages.oldPK == cont.Id_id).get()
        containersModel.Containers(
                chemId              = relChemId.chemId,
                storageId           = relStorId.sId,
                barcodeId           = cont.UniqueContainerID,
                currentQuantityUnit = "G",
                currentQuantity     = 4.0,
                capacity            = 5.0,
                receiveDate= cont.ReservedDate,
                migrated            = 1).save()
        #print cont.UniqueContainerID + " was added to Containers"i
    print "Containers were added to the database"
    ####
    #Init container histories
    ####
    newCons = Containers.select()
    for newcon in newCons:
        currentQuant = str(newcon.currentQuantity) + str(newcon.currentQuantityUnit)
        historiesModel.Histories(
            movedTo       = newcon.storageId,
            containerId   = newcon.conId,
            action        = "Created",
            pastQuantity  = currentQuant
            ).save()
    print "Initial Container Histories Created"
    ####
    # Make all testing users
    ####
    usersModel.Users(
        username = "ballz",
        auth_level = "admin",
        emailadd = "Does this matter?",
        reportto = "Does this matter either?",
        approve = True).save()

    usersModel.Users(
        username = "hooverk",
        auth_level = "systemAdmin",
        emailadd = "Does this matter?",
        reportto = "Does this matter either?",
        approve = True).save()

    usersModel.Users(
        username = "thakurr",
        auth_level = "superUser",
        emailadd = "Does this matter?",
        reportto = "Does this matter either?",
        approve = True).save()

    usersModel.Users(
        username = "williamsk",
        auth_level = "systemUser",
        emailadd = "Does this matter?",
        reportto = "Does this matter either?",
        approve = True).save()

    usersModel.Users(
        username = "heggens",
        auth_level = "systemUser",
        emailadd = "Does this matter?",
        reportto = "Does this matter either?",
        created_by = "thakurr",
        end_date = "08/16/2017").save()
        
    usersModel.Users(
        username = "settersz",
        auth_level = "systemUser",
        emailadd = "settersz@berea.edu",
        reportto = "I REPORT TO NO MAN!",
        created_by = "ballz",
        end_date = "10/31/2025").save()
        
    usersModel.Users(
        username = "whismanc",
        auth_level = "systemUser",
        emailadd = "I don't care",
        reportto = "Someone",
        created_by = "thakurr",
        end_date = "08/16/2017").save()
    
    print "Test Users were added to the database"

init_db()
