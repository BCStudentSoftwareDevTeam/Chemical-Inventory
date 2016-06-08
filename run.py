# Run a test server.
from application import app
from config import *

app.run(debug = config.sys.debug)
