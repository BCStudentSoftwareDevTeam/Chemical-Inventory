from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckOut a container
@app.route('/sa/CheckOut/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
def saCheckOut():
  return render_template("views/sa/saCheckOutView.html", config = config)

