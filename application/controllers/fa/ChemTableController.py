from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Shows all Chemicals in Database.
@app.route('/fa/ChemTable/', methods = ['GET'])
@require_role('faculty')
def faChemTable():
    chemicals = chemicalsModel.Chemicals.select()
    return render_template("views/fa/ChemTableView.html", config = config, chemicals= chemicals)

