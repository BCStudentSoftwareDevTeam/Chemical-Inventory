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
    roomsList = Rooms.select()# To create a list of possible storage locations
    # This query assumes that containers may only be stored in a room if it has a storage unit
    # Waiting for feedback from Kye on this
    print roomsList
    if request.method == "GET":
        return render_template("views/ma/AddContainerView.html",
                               config = config,
                               contConfig = contConfig,
                               chemName = chemName,
                               chemId = chemId)
    data = request.form
    modelData, extraData = sortPost(data, Containers)
    Containers.create(**modelData)
    return render_template("views/ma/AddContainerView.html",
                           config = config,
                           contConfig = contConfig,
                           chemName = chemName,
                           chemId = chemId)

