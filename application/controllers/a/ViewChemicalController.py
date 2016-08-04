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
@app.route('/a/ViewChemical/<chemical>/<chemId>/', methods = ['GET'])
@require_role('systemUser')
def aViewChemical(chemical, chemId):
  chemInfo = Chemicals.get(Chemicals.chemId == chemId) #Get chemical by correct chemId
  if chemInfo.remove == True: #If the chemical attribute, 'remove', was set to True, go back to the chemical table.
    return redirect('a/ChemTable')
  containers = (((Containers
                .select())
                .join(Chemicals))
                .where(
                  (Containers.chemId == chemId) &
                  (Containers.disposalDate == None)
                ))
  #(Above) Get all containers of this chemical that haven't been disposed of
  return render_template("views/a/ViewChemicalView.html",
                         config = config,
                         chemInfo = chemInfo,
                         containers = containers,
                         contConfig = contConfig,
                         chemConfig = chemConfig,
                         quote = quote)

