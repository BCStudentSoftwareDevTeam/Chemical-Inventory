from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role
from urllib import *

from flask import \
    render_template, \
    request, \
    jsonify, \
    url_for

# PURPOSE: Shows all Chemicals in Database.
@app.route('/ma/ChemTable/', methods = ['GET'])
@require_role('admin')
def maChemTable():
  chemicals = Chemicals.select() #Get all chemicals from the database
  contDict = {} #Set up a dictionary for all containers
  for chemical in chemicals: #For each chemical
    contDict[chemical.name] = ((((Chemicals
                              .select())
                              .join(Containers))
                              .where(
                                (Containers.disposalDate == None) &
                                (Containers.chemId == chemical.chemId) &
                                (Containers.checkedOut == False)&
                                (Chemicals.remove == False))
                              .count()))
  #(Above) Set value for the chemicals name to a count of how many containers of this chemical that are not checked out, and have not been disposed of
                              
  return render_template("views/ma/ChemTableView.html",
                          config = config, 
                          chemicals = chemicals, 
                          contDict = contDict,
                          quote = quote)
                          
@app.route("/getEditData/", methods = ['GET']) #AJAX call to get data for edit chemical form
def getEditData():
    chemId = request.args.get('chemId')
    chemical = Chemicals.select().where(Chemicals.chemId ==  chemId).dicts().get() # Gets the database entry as a dictionary. This is needed to pass it as a JSON object
    for key in chemical:
      chemical[key] = str(chemical[key]) #Set all values to a string. This is needed for jsonify
    return jsonify(chemical)