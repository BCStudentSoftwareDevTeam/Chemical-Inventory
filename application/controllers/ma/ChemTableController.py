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
@app.route('/ma/ChemTable/', methods = ['GET'])
@require_role('admin')
def maChemTable():
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
  # containers = Containers.select().where(Containers.disposalDate == None)
  # contDict = {}
  # for container in containers:
  #   for chemical in chemicals:
  #     contDict[chemical.name] = 0
  #     if container.chemId == chemical:
  #         contDict[chemical.name] += 1
  return render_template("views/ma/ChemTableView.html",
                          config = config, 
                          chemicals = chemicals, 
                          contDict = contDict)

