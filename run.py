# Import the Flask instance (app) from the application
from application import app
# Import all of our configuration
from application.config import *
# Import logging
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
handler = RotatingFileHandler('/data/chemical.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Run the web application.
app.run(debug = config.sys.debug, host = config.sys.host, port = config.sys.port)
