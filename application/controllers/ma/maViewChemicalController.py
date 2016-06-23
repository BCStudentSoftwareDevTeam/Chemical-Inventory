from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Shows specific chemical and all containers of said chemical.
@app.route('/ma/ViewChemical/<string:chemical>/', methods = ['GET'])
@require_role('admin')
def maViewChemical(chemical):
  return render_template("views/ma/maViewChemicalView.html", config = config)

