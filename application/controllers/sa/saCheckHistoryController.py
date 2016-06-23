from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Check history of a specific chemical
@app.route('/sa/CheckHistory/<string:chemical>/', methods = ['GET'])
@require_role('systemAdmin')
def saCheckHistory(chemical):
  return render_template("views/sa/saCheckHistoryView.html", config = config)

