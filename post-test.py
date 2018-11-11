#!/usr/bin/python

import requests
import datetime
import random
import os, sys
import time

ids = ['192423556']
#ids = ['192423556', '47895486', '256083609']

pos = (59.939013, 30.318338)

if len(sys.argv) != 2:
    exit("usage: {} addr".format(sys.argv[0]))

for user_id in ids:
    payload = {
        "user_id": user_id,
        "lat": str(pos[0] + random.random() * 0.001),
        "lng": str(pos[1] + random.random() * 0.001),
        "time": str(datetime.datetime.now()),
        "presence": str(False),
        "name": ""
    }
    r = requests.post("http://" + sys.argv[1] + "/submit", json=payload)
