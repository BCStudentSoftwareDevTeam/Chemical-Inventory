from application import app
from application.models.batchModel import *
from application.models.mainModel import * 
from application.models.locatesModel import *
from application.models.roomsModel import *
from application.config import *


from flask import render_template
@app.route('/ma/migrateChem/', methods = ['GET', 'POST'])
def maMigrateChem():
    location = Batch.select()
    locdict = Batch.select().dicts().get()
   
    return render_template("views/ma/MigrateChem.html",
				    location = location,
				    locdict = locdict,
                                    config = config)
