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
  return render_template("views/ma/maChemTableView.html", config = config)

