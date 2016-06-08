# WARNING
# This script deletes the database file and configures empty
# tables for the models defined in the models module.
from application import app
from application import models
from config import *
import os

def init_db ():
    """Initializes the database."""
    global db_models
    # Remove the DB
    if os.path.isfile(config.database.filename):
      os.remove(config.database.filename)

    # Create an empty DB file
    open(config.database.filename, 'a').close()

    for m in models.models:
      print("Creating {0}".format(m))
      m.create_table()

    print 'Initialized the database.'


if __name__ == "__main__":
  init_db()
