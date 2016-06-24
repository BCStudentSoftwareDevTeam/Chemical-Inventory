from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Dashboard and homepage for the Admin
@app.route('/ma/Home/', methods = ['GET'])
@require_role('admin')
def adminHome():
  return render_template("views/ma/HomeView.html", config = config)

