from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Edit, delete, and add buildings
@app.route('/ma/ManageBuildings/', methods = ['GET', 'POST'])
@require_role('admin')
def ManageBuildings():
    buildings = buildingsModel.Buildings.select()
    floors = floorsModel.Floors.select()
    rooms = roomsModel.Rooms.select().order_by(+roomsModel.Rooms.name)
    storages = storagesModel.Storages.select()
    return render_template("views/ma/ManageBuildingsView.html",
                           config = config,
                           locationConfig = locationConfig,
                           buildings = buildings,
                           floors = floors,
                           rooms = rooms,
                           storages = storages)

