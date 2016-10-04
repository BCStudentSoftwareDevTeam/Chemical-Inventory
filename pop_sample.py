from application.models import classes 
from applicaion.config import *
from applicatoin.models import *
import datetime

def init_db():
    #Create the databases
    for database in config.databases:
        filename = config.databases[database].filename
        
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
main_table = Main.select().get()
print main_table
