# Import the Flask instance (app) from the application
from application import app
# Import all of our configuration
from config import *

# Run the web application.
app.run(debug = config.sys.debug)
