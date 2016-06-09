# WARNING
# This script deletes the database file and configures empty
# tables for the models defined in the models module.
from application.models import models, classes
from config import *
    
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
    

if __name__ == "__main__":
  init_db()
