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
@app.route('/sa/ChemTable/', methods = ['GET'])
@require_role('systemAdmin')
def saChemTable():
  chemicals = Chemicals.select()
  contDict = {}
  for chemical in chemicals:
    print "Here"
    contDict[chemical.name] = (((Chemicals
                              .select()
                              .join(Containers))
                              .where(
                                (Containers.disposalDate == None) &
                                (Containers.chemId == chemical.chemId) &
                                (Containers.checkedOut == False)&
                                (Chemicals.remove == False))
                              .count()))
                              
  
  return render_template("views/sa/ChemTableView.html",
                          config = config, 
                          chemicals = chemicals, 
                          contDict = contDict,
                          quote = quote)

