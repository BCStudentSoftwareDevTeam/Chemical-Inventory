from application import app
from application import models
from config import *
import inspect
import peewee

import os

def init_db ():
    """Initializes the database."""
    # Remove the DB
    if os.path.isfile(config.database.filename):
      os.remove(config.database.filename)
    
    # Create an empty DB file
    open(config.database.filename, 'a').close()
    
    db_models = [models.Mess]

    for m in db_models:
      print("Creating {0}".format(m))
      m.create_table()
    
    print 'Initialized the database.'


if __name__ == "__main__":
  init_db()