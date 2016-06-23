from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Edit, delete, and add floors and rooms
@app.route('/ma/ManageFloors/', methods = ['GET', 'POST'])
@require_role('admin')
def ManageFloors():
  return render_template("views/ma/ManageFloorsView.html", config = config)

