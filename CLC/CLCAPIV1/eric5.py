# -*- coding: utf-8 -*-
"""
Created on Friday 2 12 2016

@author: IAMGHOST eric.lucas@centurylink.com
"""
#!/usr/bin/env python

import requests
import json

headers = {'content-type': 'application/json'}
payload = {'APIKey': ‘xxxxxx’, 'Password': ‘xxxxx’}

#CTS/Tier3 Authentication - Requires getting session cookie, save use later
r = requests.post("https://api.ctl.io/REST/Auth/Logon", data=payload)
#Simple Output of Login Attempt Success/Failure
print r
print r.text
#Get All Servers Currently Deployed in CTS/CenturyLink Cloud
r1 = requests.post("https://api.ctl.io/REST/Account/GetAccounts/JSON", data=json.dumps(payload), cookies=r.cookies, headers=headers)
print r1
print r1.json()
