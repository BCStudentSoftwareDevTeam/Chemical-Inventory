from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role
from urllib import *
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    redirect, \
    url_for

# PURPOSE: Shows specific chemical and all containers of said chemical.
@app.route('/ma/ViewChemical/<chemical>/<chemId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maViewChemical(chemical, chemId):
  chemInfo = Chemicals.get(Chemicals.name == chemical)
  chemDict = Chemicals.select().where(Chemicals.name == chemical).dicts().get()
  print "From Database: %s" %(chemDict)
  if chemInfo.remove == True:
    return redirect('ma/ChemTable')
  if request.method == "POST":
    data = request.form
    for i in data:
      var = setattr(chemInfo, i, data[i])
    chemInfo.save()
    return redirect('/ma/ViewChemical/%s/%s/' %(chemInfo.name, chemInfo.chemId))
  containers = (((Containers
                .select())
                .join(Chemicals))
                .where(
                  (Containers.chemId == chemId) &
                  (Containers.disposalDate == None)
                ))
  return render_template("views/ma/ViewChemicalView.html",
                         config = config,
                         chemInfo = chemInfo,
                         containers = containers,
                         contConfig = contConfig,
                         chemConfig = chemConfig)
                         
@app.route('/ma/ViewChemical/<chemical>/<chemId>/delete/', methods = ['GET','POST'])
def maDeleteChemical(chemical, chemId):
  chem = Chemicals.get(Chemicals.chemId == chemId)
  chem.deleteDate = datetime.date.today()
  chem.remove = True
  chem.save()
  return redirect('/ma/ChemTable')
