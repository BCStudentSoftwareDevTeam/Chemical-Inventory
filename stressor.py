#!/usr/bin/env python
from application.models import Mess
from config import *
from httplib import *
from urllib import *
from uuid import *

import string
import random

def generate (size = 6, chars = string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
numInserts = 1000

for stringSize in [256, 512, 1024, 4096, 65536]:
  myID = uuid4()
  s = generate(stringSize)
  for i in range (numInserts):
    conn      = HTTPConnection(config.sys.host, config.sys.port)
    # print("String generated: {0}".format(s))
    # print "Insert #{0}".format(i)
    params = urlencode({'id': myID, 'data': s})
    conn.request("POST", "insert", params, headers)
    response = conn.getresponse()
    if response.status != 200:
      print "Error on insert {0}: {1} {2}".format(i, response.status, response.reason)

  inserted = Mess.select().where(Mess.id == myID).count()
  if inserted == numInserts:
    print ("{1} inserts of size {0} successful.".format(stringSize, numInserts))
  else:
    print ("Inserted {0}, found {1} in the DB.".format(numInserts, numInserts - inserted))