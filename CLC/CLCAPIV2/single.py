#!/usr/bin/python
## Eric Lucas Single Build Make Managed Server 
## Centurylink API V2 

import json
import requests


headers = {'content-type': 'application/json'}
payload = {'username': ‘xxxxxx’, 'password': ‘xxxxxxx’}

r = requests.post("https://api.ctl.io/v2/authentication/login", data=payload)
print r
p = json.loads(r.text)
print json.dumps(p, indent=4, sort_keys=True)
headers['Authorization'] = "Bearer " + p['bearerToken'].encode('utf-8')
 

#Authenticate

r = requests.post("https://api.ctl.io/REST/Auth/Logon", data=payload)

print "Authenticated"


#Create a make managedOS, make managed backup and additional disk
payload2 = {"name": "melcor","description": “test”,”groupid": “0000000000000”,”sourceserverid": “TEMPLATESERVER”,”ismanagedos": "true","ismanagedbackup": "false","primarydns": "172.1.1.1”,”secondarydns": "172.1.1.1”,”networkid": “00000000000”,”ipaddress": "","password": "","sourceserverpassword": "","cpu": "8","memorygb": "32","type": "standard","storagetype": "standard","additionaldisks": [{"path": "E", "sizegb": 100, "type": "partitioned"}], "ttl": "", "packages": [{"packageid": ""}]}
r1 = requests.post("https://api.ctl.io/v2/servers/XXXX/“, data=json.dumps(payload2), cookies=r.cookies, headers=headers)

print json.dumps(r1.json(), indent=4)

