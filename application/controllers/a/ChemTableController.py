from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Shows all Chemicals in Database.
@app.route('/a/ChemTable/', methods = ['GET'])
@require_role('anon')
def ChemTable():
  return render_template("views/a/ChemTableView.html", config = config)

