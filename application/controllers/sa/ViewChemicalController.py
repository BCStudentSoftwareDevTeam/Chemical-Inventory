from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role
from urllib import *

from flask import \
    render_template, \
    redirect, \
    request, \
    url_for

# PURPOSE: Shows specific chemical and all containers of said chemical.
@app.route('/sa/ViewChemical/<string:chemical>/<string:chemId>/', methods = ['GET', 'POST'])
@require_role('systemAdmin')

def saViewChemical(chemical, chemId):
  chemInfo = Chemicals.get(Chemicals.chemId == chemId) #Get chemical by correct chemId
  chemDict = Chemicals.select().where(Chemicals.chemId == chemId).dicts().get() #Get chemical by correct chemId as a dictionary
  if chemInfo.remove == True: #If the chemical attribute, 'remove', was set to True, go back to the chemical table.
    return redirect('sa/ChemTable')
  if request.method == "POST":
    data = request.form
    for i in data:
      var = setattr(chemInfo, i, data[i])
    chemInfo.save()
    return redirect('/sa/ViewChemical/%s/%s/' %(chemInfo.name, chemInfo.chemId))
  containers = (((Containers
                .select())
                .join(Chemicals))
                .where(
                  (Containers.chemId == chemId) &
                  (Containers.disposalDate == None)
                ))
  #(Above) Get all containers of this chemical that haven't been disposed of
  return render_template("views/sa/ViewChemicalView.html",
                         config = config,
                         chemInfo = chemInfo,
                         containers = containers,
                         contConfig = contConfig,
                         chemConfig = chemConfig)