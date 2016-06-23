from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Check history of a specific chemical
@app.route('/ma/CheckHistory/<string:chemical>/', methods = ['GET'])
@require_role('admin')
def maCheckHistory(chemical):
  return render_template("views/ma/maCheckHistoryView.html", config = config)

