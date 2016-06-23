from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Display chemicals that are checked out
@app.route('/sa/CheckedOut/', methods = ['GET'])
@require_role('systemAdmin')
@require_role('admin')
def CheckedOut():
  return render_template("views/sa/CheckedOutView.html", config = config)

