# Import the Flask instance (app) from the application
from application import app
# Import all of our configuration
from application.config import *

# Builds the server configuration
if os.getenv('IP'):
  IP    = os.getenv('IP')
else:
  IP    = '0.0.0.0'

# Run the web application.
app.run(debug = config.sys.debug, host = config.sys.host, port = config.sys.port)
