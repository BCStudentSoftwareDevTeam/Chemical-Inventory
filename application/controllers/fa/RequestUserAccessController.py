from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: This is the homepage/dashboard for the professor
@app.route('/fa/Home/', methods = ['GET'])
@require_role('faculty')
def Home():
  return render_template("views/fa/HomeView.html", config = config)

