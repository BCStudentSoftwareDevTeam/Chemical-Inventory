# WARNING
# This script deletes the database file and configures empty
# tables for the models defined in the models module.
from application.models import models
from config import *
import importlib
import os, re

def classFromName(moduleName, className):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(moduleName)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, className)
    return c
    
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
  for m in models:  
    moduleName = "application.models.{0}".format(m) 
    className  = re.sub("Model", "", m).capitalize()
    # print "Module Name: {0}\nClass Name: {1}".format(moduleName, className)
    c = classFromName(moduleName, className)
    # print "Creating table from class: {0}".format(c)
    # The "True" parameter makes sure the table does not exist before creating.
    c.create_table(True)
    

  print 'Initialized the database.'
    

if __name__ == "__main__":
  init_db()
