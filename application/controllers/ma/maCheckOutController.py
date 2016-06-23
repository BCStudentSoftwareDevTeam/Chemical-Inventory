from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckOut a container
@app.route('/ma/CheckOut/', methods = ['GET', 'POST'])
@require_role('admin')
def maCheckOut():
  return render_template("views/ma/maCheckOutView.html", config = config)

