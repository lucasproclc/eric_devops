#!/usr/bin/env python

import requests
import json

headers = {'content-type': 'application/json'}
payload = {'APIKey': ‘xxxxxxx’, 'Password': ‘xxxxx’}

#CTS/Tier3 Authentication - Requires getting session cookie, save use later
r = requests.post("https://api.ctl.io/REST/Auth/Logon", data=payload)
#Simple Output of Login Attempt Success/Failure
print r
print r.text
#Get CLC Credentials.  
r1 = requests.post("https://api.ctl.io/REST/Server/GetAllServers/JSON", data=json.dumps(payload), cookies=r.cookies, headers=headers)
print r1
print r1.json()
