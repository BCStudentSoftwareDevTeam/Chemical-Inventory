from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role
from urllib import *

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Shows all Chemicals in Database.
@app.route('/a/ChemTable/', methods = ['GET'])
@app.route('/a/Home/', methods = ['GET'])
@require_role('systemUser')
def aChemTable():
  chemicals = Chemicals.select() #Get all chemicals from the database
  contDict = {} #Set up a dictionary for all containers
  for chemical in chemicals: #For each chemical
    contDict[chemical.name] = ((((Chemicals
                              .select())
                              .join(Containers))
                              .where(
                                (Containers.disposalDate == None) &
                                (Containers.chemId == chemical.chemId) &
                                (Containers.checkedOut == False))
                              .count()))
  #(Above) Set value for the chemicals name to a count of how many containers of this chemical that are not checked out, and have not been disposed of
  return render_template("views/a/ChemTableView.html",
                          config = config, 
                          chemicals = chemicals, 
                          contDict = contDict,
                          quote = quote)
                        
