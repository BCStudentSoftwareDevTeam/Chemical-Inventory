# Import the Flask instance (app) from the application
from application import app
# Import all of our configuration
from application.config import *
import socket
import os

# Builds the server configuration
IP = '0.0.0.0'
if os.getenv('USER'):
  hostname = os.getenv('USER')
  try:
    IP = socket.gethostbyname(hostname)
  except:
    pass

# Run the web application.
app.run(debug = config.sys.debug, host = IP, port = config.sys.port)
