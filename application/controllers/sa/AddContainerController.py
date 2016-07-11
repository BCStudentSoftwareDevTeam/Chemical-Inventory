from application import app
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Add Container for a certain chemical
@app.route('/sa/AddContainer/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
@require_role('admin')
def AddContainer():
  if request.method == "GET":
      return render_template("views/sa/AddContainerView.html", config = config, contConfig = contConfig)
  data = request.form
  modelData, extraData = sortPost(data, Containers)
  Containers.create(**modelData)
  return render_template("views/ma/AddContainerView.html", config = config, contConfig = contConfig)

