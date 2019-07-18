from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
session = LoginSession('https://192.168.250.151', 'admin', 'C!sc0123')
moDir = MoDirectory(session)
moDir.login()

from cobra.mit.request import DnQuery
from cobra.mit.request import ClassQuery

# Specify the object class
TENANTS_Q = ClassQuery("fvTenant")

# create a query for each object in the class
TENANTS = moDir.query(TENANTS_Q)

#print(dir(TENANTS))
for TENANT in TENANTS:
    print(TENANT.name)
