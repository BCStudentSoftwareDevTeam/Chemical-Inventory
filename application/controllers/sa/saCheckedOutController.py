from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Display containers that are checked out
@app.route('/sa/CheckedOut/', methods = ['GET'])
@require_role('systemAdmin')
def saCheckedOut():
  return render_template("views/sa/saCheckedOutView.html", config = config)

