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

for tenant in session.query(ClassQuery("fvTenant")):

  print('Tenant: {0}'.format( tenant.name))

  ap_Q = ClassQuery('fvAp')
  ap_Q.dn = tenant.dn
  
  for ap in session.query(ap_Q): 
    print('  Application Profile: {0}'.format(ap.name)) 

  tenantSubtree_Q = DnQuery(tenant.dn)
  tenantSubtree_Q.subtree = 'children'
  
  
    

#Query Fabric Nodes

for fabricNode in session.query(ClassQuery("fabricNode")):
  print('Frabic Node: {}'.format(fabricNode.name))





session.logout()
