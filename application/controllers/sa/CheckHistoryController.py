from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Check history of a specific chemical
@app.route('/sa/CheckHistory/<chemical>/', methods = ['GET'])
@require_role('systemAdmin')
@require_role('admin')
def CheckHistory(chemical):
  return render_template("/views/sa/CheckHistoryView.html", config = config)


