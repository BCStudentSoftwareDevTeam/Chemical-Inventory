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
@app.route('/sa/ViewChemical/<string:chemical>/<string:chemId>/', methods = ['GET'])
@require_role('systemAdmin')
def saViewChemical(chemical, chemId):
  chemInfo = Chemicals.get(Chemicals.name == chemical)
  if chemInfo.remove == True:
    return redirect('sa/ChemTable')
  containers = (((Containers
                .select())
                .join(Chemicals))
                .where(
                  (Containers.chemId == chemId) &
                  (Containers.disposalDate == None)
                ))
  return render_template("views/sa/ViewChemicalView.html",
                         config = config,
                         chemInfo = chemInfo,
                         containers = containers,
                         contConfig = contConfig,
                         chemConfig = chemConfig,
                         quote = quote)