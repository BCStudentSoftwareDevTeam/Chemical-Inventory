from application.models import classes 
from application.config import *
from application.models import *
from application.models.staticModels.batchModel import *
from application.models.staticModels.mainModel import * 
from application.models.staticModels.locatesModel import *
from application.models.chemicalsModel import *
from application.models.roomsModel import *
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
        #Translate the form
        state_map = {'0':"Solid", '1':"Liquid",'2':"Gas"}
        state = state_map[chem.State]

        #Translate the structure
        if chem.Organic == 1:
            struct = "Organic"
        elif chem.Inorganic == 1:
            struct = "Inorganic"
        else:
            struct = "Unknown"

        #Translate Hazards
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
        
        chemicalsModel.Chemicals(
            oldPK          = chem.NameSorted,
            name           = chem.NameRaw,
            casNum         = chem.casNo,
            primaryHazard  = chem.Id3,
            formula        = chem.StructuralFormula,
            state          = state,
            structure      = struct,
            description    = chem.PhysicalDescription,
            healthHazard   = chem.Nfpa_Health,
            flammable      = chem.Nfpa_Flamable,
            reactive       = chem.Nfpa_Reactive,
            boilPoint      = chem.BoilingPoint,#float(chem.BoilingPoint),
            molecularWeight= chem.molecularWeight,#float(chem.molecularWeight),
            flamePict      = chem.Flamable,#bool(chem.Flamable),
            hhPict         = hhazard,
            gcPict         = gascylinder,
            corrosivePict  = chem.Corrosive, #bool(chem.Corrosive),
            expPict        = chem.Explosive,#bool(chem.Explosive),
            oxidizerPict   = oxidizer).save()
        print chem.NameRaw + " was added to the database"
    
    ####
    #Import LOCATES Table from CISPro into inventory.sqlite
    ###
    locates_table = Locates.select()
    for location in locates_table:
        roomsModel.Rooms(
                oldPK      = location.Location,
                floorId    = 0,
                name       = location.NameSorted).save()
        print location.NameSorted + " was added to ROOMS"

    ####
    #Import BATCHES Table from CISPro into inventory.sqlite
    ####
    cont_table = Batch.select()
    for cont in cont_table:
        relChemId = Chemicals.select().where(cont.NameRaw == Chemicals.oldPK) #You were changing this and realized that it it querying the wrong database for the cont.NameRaw
        relStorId = Rooms.select().where(Rooms.oldPK == cont.Id)
        containersModel.Containers(
                chemId     = relChemId.chemId,
                storageId  = relStorId.conId,
                barcodeId  = cont.UniqueContainerID,
                receiveDate= cont.ReservedDate).save()
        print cont.UniqueContainerID + " was added to Containers"

init_db()
