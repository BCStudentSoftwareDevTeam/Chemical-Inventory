from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckOut a chemical
@app.route('/sa/CheckOut/<chemId>/<conId>/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
@require_role('admin')
def CheckOut(chemId, conId):
    chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
    container = containersModel.Containers.get(containersModel.Containers.conId == conId)
    return render_template("views/sa/CheckOutView.html", config = config, container = container, chemical = chemical)

