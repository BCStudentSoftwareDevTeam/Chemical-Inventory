from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Add Chemical to the database
@app.route('/ma/AddChemical/', methods = ['GET', 'POST'])
@require_role('admin')
def maAddChemical():
  return render_template("views/ma/AddChemicalView.html", config = config)

