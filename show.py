HOST='https://192.168.250.151'
USER='admin'
PASS='C!sc0123'

from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession

from cobra.mit.request import DnQuery
from cobra.mit.request import ClassQuery

#login Session
session = LoginSession(HOST, USER, PASS)
moDir = MoDirectory(session)
moDir.login()

# Specify the object class
TENANTS_Q = ClassQuery("fvTenant")

# create a query for each object in the class
TENANTS = moDir.query(TENANTS_Q)

#print(dir(TENANTS))
for TENANT in TENANTS:
    print('Tenant: {}'.format(TENANT.name))
