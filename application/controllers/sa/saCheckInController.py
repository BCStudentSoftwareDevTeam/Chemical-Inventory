from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckIn a container
@app.route('/sa/CheckIn/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
def saCheckIn():
  return render_template("views/sa/saCheckInView.html", config = config)

