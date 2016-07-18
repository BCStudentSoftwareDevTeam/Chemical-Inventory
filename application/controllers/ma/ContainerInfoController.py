from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role
from datetime import *

from flask import \
    render_template, \
    request, \
    redirect, \
    url_for

# PURPOSE: CheckOut a container
@app.route('/ma/ContainerInfo/<chemId>/<conId>/', methods = ['GET', 'POST'])
@require_role('admin')
def maContainerInfo(chemId, conId):
  chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.chemId == chemId)
  container = containersModel.Containers.get(containersModel.Containers.conId == conId)
  storageList = storagesModel.Storages.select()
  buildingList = buildingsModel.Buildings.select()
  if request.method =="POST":
    try:
      if request.form['dispose'] == "Dispose of this Container":
        container.disposalDate = datetime.now()
        container.save()
        return redirect(url_for("maChemTable"))
    except:
      data = request.form
      cont = containersModel.Containers.get(conId = conId)
      cont.forClass  = data['class']
      cont.checkedOut = True
      cont.forProf = data ['forProf']
      cont.storageId.roomId.floorId.buildId = data['storageId']
      cont.save()
      # add form data to container as checked out
      return redirect('/ma/ViewChemical/' + chemical.name + '/' + chemId + '/')
  else:
    return render_template("views/ma/ContainerInfoView.html",
                       config = config,
                       container = container,
                       chemical = chemical,
                       storageList = storageList,
                       buildingList = buildingList)