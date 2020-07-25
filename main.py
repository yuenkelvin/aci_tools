#!/usr/bin/env python3

import json
import sys
import urllib3
import apic
from apicObjModel import ApicObjModel
import apicObj

def main():
    
    apic_ip = 'localhost'
    apic_port = '16214'
    apic_user = 'admin'
    apic_password = 'Col1@3col1@3Col'

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    rc = apic.ApicRestClient(apic_ip, apic_port, apic_user, apic_password)
    
    
    test = apicObj.fvAEPg(rc).raw


    print(json.dumps(test, indent=4)) 


if __name__ == '__main__':

    sys.exit(main())

