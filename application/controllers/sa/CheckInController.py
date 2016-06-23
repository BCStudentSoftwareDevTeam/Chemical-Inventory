from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckIn a chemical
@app.route('/sa/CheckIn/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
@require_role('admin')
def CheckIn():
  return render_template("views/sa/CheckInView.html", config = config)

