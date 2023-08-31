# About This Application

To build this application you must...
1. Run the setup file with the command
	source setup.sh

2. Populate the database with test values or a production backup
	database/reset-database.sh [test|from-backup]

3. Add your current machine user id to admin in config/role.yaml 

4. Start Appache server to serve application
	flask run

5. Open 127.0.0.1:8080 in your browser (or whatever IP flask gives you)

# Relevant Documentation

To work on this application, you'll probably want:

* The Flask Documentation

  http://flask.pocoo.org/

* The Jinja Documentation

  http://jinja.pocoo.org/docs/dev/

* The PeeWee Documentation

  http://docs.peewee-orm.com/en/latest/index.html

That's most of what comes to mind...
