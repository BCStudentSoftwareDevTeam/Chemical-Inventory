from application import app
from application.config import *
from application.logic.getAuthUser import AuthorizedUser
from application.logic.excelMaker import exportExcel


from flask import render_template, \
                  request, \
                  flash, \
                  redirect, \
                  url_for

@app.route('/Report/', methods = ['GET', 'POST'])
def report():
    auth = AuthorizedUser()
    user = auth.getUser()
    userLevel = auth.userLevel()

    if userLevel == 'admin':
        if request.method == "GET":
            return render_template("views/ReportView.html",
                                   authLevel = userLevel,
                                   config = config)
        else:
            data = request.form
            exportExcel(data['test'])
            return redirect(url_for("report"))
