#!/usr/bin/env python3

import sys
import requests
token = 'token'
lumiasend = 'http://localhost:39231/api/send?token='

x = str(sys.argv[1])
y = str(sys.argv[2])
requests.post(lumiasend + token, data={'type':x,'value':y})
