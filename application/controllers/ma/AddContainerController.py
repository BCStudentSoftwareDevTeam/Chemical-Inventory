from application import app
from application.models.containersModel import *
from application.models.roomsModel import *
from application.models.storagesModel import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Add Container for a certain chemical
@app.route('/ma/AddContainer/<chemName>/<chemId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maAddContainer(chemName, chemId):
  chemInfo = Chemicals.get(Chemicals.chemId == chemId)
  if request.method == "GET":
      return render_template("views/ma/AddContainerView.html",
                             config = config,
                             contConfig = contConfig,
                             chemInfo = chemInfo)
  data = request.form
  modelData, extraData = sortPost(data, Containers)
  print modelData
  Containers.create(**modelData)
  return render_template("views/ma/AddContainerView.html",
                         config = config,
                         contConfig = contConfig,
                         chemInfo = chemInfo)