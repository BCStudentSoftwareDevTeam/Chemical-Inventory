# About This Application

To build this application you must...
1. Have python 2.7 and `virtualenv` installed
2. Run the setup file with the command
	source setup.sh
3. Populate the database with generic values
	python reset-db.py
4. Add your current machine user id to admin in config/roles.yaml 
5. Start webserver to serve application
	python run.py
6. Open 0.0.0.0:8080 in your browser if you are working locally, your IP:8080 if remotely

# Relevant Documentation

To work on this application, you'll probably want:

* The Flask Documentation

  http://flask.pocoo.org/

* The Jinja Documentation

  http://jinja.pocoo.org/docs/dev/

* The PeeWee Documentation

  http://docs.peewee-orm.com/en/latest/index.html

* The Configure Documentation

  http://configure.readthedocs.io/en/latest/#

That's most of what comes to mind...
