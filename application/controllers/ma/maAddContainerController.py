from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Add Container for a certain chemical
@app.route('/ma/AddContainer/', methods = ['GET', 'POST'])
@require_role('admin')
def maAddContainer():
  return render_template("views/ma/maAddContainerView.html", config = config)

