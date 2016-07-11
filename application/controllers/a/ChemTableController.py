from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Shows all Chemicals in Database.
@app.route('/a/ChemTable/', methods = ['GET'])
@require_role('systemUser')
def aChemTable():
  chemicals = Chemicals.select()
  contDict = {}
  for chemical in chemicals:
    contDict[chemical.name] = ((((Chemicals
                              .select())
                              .join(Containers))
                              .where(
                                (Containers.disposalDate == None) &
                                (Containers.chemId == chemical.chemId)))
                              .count())
  return render_template("views/ma/ChemTableView.html",
                          config = config, 
                          chemicals = chemicals, 
                          contDict = contDict)
