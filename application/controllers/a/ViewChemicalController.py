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

# PURPOSE: Shows specific chemical and all containers of said chemical.
@app.route('/a/ViewChemical/<chemical>/<chemId>/', methods = ['GET'])
@require_role('systemUser')
def aViewChemical(chemical, chemId):
  chemInfo = Chemicals.get(Chemicals.name == chemical)
  containers = (((Containers
                .select())
                .join(Chemicals))
                .where(Containers.chemId == chemId))
  return render_template("views/a/ViewChemicalView.html",
                         config = config,
                         chemInfo = chemInfo,
                         containers = containers,
                         contConfig = contConfig,
                         chemConfig = chemConfig,
                         quote = quote)

