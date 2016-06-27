from application import app
from application.models import *
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
  chemicals = chemicalsModel.Chemicals.select()
  return render_template("views/ma/ChemTableView.html", config = config, chemicals = chemicals)

