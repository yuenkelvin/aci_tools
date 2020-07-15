#!/usr/bin/env python3

import json
import sys
import apic
import urllib3

apic_ip = 'localhost'
apic_port = '16114'
apic_admin = 'admin'
apic_password = 'Col1@3col1@3Col'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

rc = apic.ApicRestClient(apic_ip, apic_port, apic_admin, apic_password)

apic_url = '/api/node/class/fvBD.json?query-target=subtree&target-subtree-class=fvBD&rsp-subtree=full&rsp-subtree-class=fvSubnet,fvRsCtx'

r = rc.get(apic_url).text 
parsed_json = json.loads(r)

print(json.dumps(parsed_json['imdata'][10], indent=4))