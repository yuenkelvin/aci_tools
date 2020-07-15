#!/usr/bin/env python3

import json
import sys
import mso
import urllib3
import pprint

'''
try:
    from credentials import MSO_IP, MSO_ADMIN, MSO_PASSWORD
except ImportError:
    sys.exit("Error: please verify credentials file format.")
'''


mso_ip = 'localhost'
mso_port = '16334'
mso_admin = 'admin'
mso_password = 'Col1@3col1@3Col'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#rc = mso.RestClient(MSO_IP, MSO_ADMIN, MSO_PASSWORD)
rc = mso.MsoRestClient(mso_ip, mso_port, mso_admin, mso_password)


# first, let's list all users
resp = rc.get('/users')
allSites = json.loads(resp.text)
for site in allSites['users']:
    queryString = '/users/' + site['id']
    siteInfo = rc.get(queryString)
    siteData = json.loads(siteInfo.text)
    siteName = siteData['username']
    print("Site {} [name {}] info".format(site['id'],siteName))
    print(80 * "=")
    pprint.pprint(siteData)
