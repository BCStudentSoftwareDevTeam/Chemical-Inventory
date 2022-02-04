# Import the Flask instance (app) from the application
from application import app
# Import all of our configuration
from application.config import *
import socket

# Builds the server configuration

if socket.gethostname():
  hostname = socket.gethostname()
  IP = socket.gethostbyname(hostname)
else:
  IP    = '0.0.0.0'


# Run the web application.
app.run(debug = config.sys.debug, host = IP, port = config.sys.port)
