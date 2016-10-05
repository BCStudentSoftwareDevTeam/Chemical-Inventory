from application.models import classes 
<<<<<<< HEAD
from application.config import *
from application.models import *
from application.models.staticModels.batchModel import *
from application.models.staticModels.mainModel import * 
from application.models.staticModels.locatesModel import *
=======
from applicaion.config import *
from applicatoin.models import *
>>>>>>> 70461f0a338b4a029d016ede65a1018aff821fa0
import datetime

def init_db():
    #Create the databases
<<<<<<< HEAD
    for database in config.databases.dynamic:
        filename = config.databases.dynamic[database].filename
=======
    for database in config.databases:
        filename = config.databases[database].filename
>>>>>>> 70461f0a338b4a029d016ede65a1018aff821fa0
        
        #Remove the DB
        if os.path.isfile(filename):
            os.remove(filename)
        
        #create an empty DB file
        open(filename, 'a').close()
    
    #Go through modules in models directory, and create a table for each one
    for c in classes:
        c.create_table(True)

    print 'Database Initialized'

#Now retreive all data from the MAIN table in CISPro
<<<<<<< HEAD
main_table = Main.select()
main_att = Main.select().dicts().get()
for chem in  main_table:
    #Translate the form
    if chem.State == 0:
        state = "Solid"
    elif chem.State == 1:
        state = "Liquid"
    elif chem.State == 2:
        state = "Gas"
    else:
        state = "N/A"

    #Translate the structure
    if chem.Organic == 1:
        structure = "Organic"
    elif chem.Inorganic == 1:
        structure = "Inorganic"
 
    chemicalsModel.Chemicals(
            chemId         = chem.NameSorted,
            name           = chem.NameRaw,
            casNum         = chem.casNo,
            primaryHazard  = chem.Id3,
            formula        = chem.StructuralFormula,
            state          = state,
            structure      = structure,
            description    = chem.PhysicalDescription,
            healthHazard   = chem.Nfpa_Health,
            flammable      = chem.Nfpa_Flamable,
            reactive       = chem.Nfpa_Reactive
            flashPoint     = 
            
            #Finish filling in this shit
        print getattr(chem, att)
=======
main_table = Main.select().get()
print main_table
>>>>>>> 70461f0a338b4a029d016ede65a1018aff821fa0
