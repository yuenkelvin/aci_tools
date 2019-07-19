APIC_HOST='192.168.250.151'
APIC_USER='admin'
APIC_PASS='C!sc0123'

APIC_URL='https://'+APIC_HOST

import urllib3

from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession

from cobra.mit.request import DnQuery
from cobra.mit.request import ClassQuery

#Gloabl Settings
urllib3.disable_warnings()

#login Session
authentication = LoginSession(APIC_URL, APIC_USER, APIC_PASS)
session = MoDirectory(authentication)
session.login()

#Query Tenant
tenants = session.query(ClassQuery("fvTenant"))
for tenant in tenants:

  print('Tenant: {} {}'.format( tenant.name, tenant.dn))

  aps = session.lookupByClass('fvAp', parentDn=tenant.dn)
  for ap in aps: 

    print('  - AP: {}'.format(ap.name)) 

    epgs = session.lookupByClass('fvAEPg', parentDn=ap.dn)
    for epg in epgs: 
 
      print('    - EPG: {}'.format(epg.name)) 
    

#Query Fabric Nodes

for fabricNode in session.query(ClassQuery("fabricNode")):
  print('Frabic Node: {}'.format(fabricNode.name))





session.logout()
