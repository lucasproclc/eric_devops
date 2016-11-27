#!/usr/bin/env python

import requests
import csv
import json
import StringIO

#Get this information from the CenturyLink Cloud Portal
payload = {'APIKey': 'xxxxxx', 'Password': 'xxxxx'}

#Headers needed for api 1.0
headers = {'content-type': 'application/json'}
#Authenticate and get cookie
r = requests.post("https://api.ctl.io/REST/Auth/Logon", data=payload)
#Simple Output of Login Attempt Success/Failure
print "Authenticated"
# for debugging
#print r
#print r.text

#Open the CSV and parse headers
f = open( './ServerList.csv', 'rU' )
reader = csv.DictReader( f, fieldnames = ( "accountalias", "name" ))

# Parse the CSV into JSON
out = "\n".join([json.dumps(row) for row in reader])
print "JSON parsed!"
print out

#Looping through JSON as lines of text
s = StringIO.StringIO(out)
next(s)
for line in s:
    payload = line
    print "About to build "+ payload
     #Post Create Server Request
    r1 = requests.post("https://api.ctl.io/REST/Server/GetServerCredentials/JSON", data=json.dumps(eval(payload)), cookies=r.cookies, headers=headers)
    print r1
    print r1.json()

print "Compelete"
