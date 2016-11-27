#!/usr/bin/python

import json
import requests


headers = {'content-type': 'application/json'}
payload = {'username': 'eric.lucas.demo', 'password': 'xxxx'}

r = requests.post("https://api.ctl.io/v2/authentication/login", data=payload)
print r
p = json.loads(r.text)
print json.dumps(p, indent=4, sort_keys=True)
headers['Authorization'] = "Bearer " + p['bearerToken'].encode('utf-8')
 

#Authenticate

r = requests.post("https://api.ctl.io/REST/Auth/Logon", data=payload)

print "Authenticated"


#Create an intra data Center Firewall Policy
payload2 = {"destinationAccount": "CCEL","source": ["10.0.0.0/24"], "destination": ["10.1.1.0/24"],"ports": ["tcp/443"]}
r1 = requests.post("https://api.ctl.io/v2-experimental/firewallPolicies/CCEL/UC1/", data=json.dumps(payload2), cookies=r.cookies, headers=headers)

print json.dumps(r1.json(), indent=4)



