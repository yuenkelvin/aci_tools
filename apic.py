#!/usr/bin/env python3
# Minimal APIC SDK v1.0
#
#

import requests
import warnings
import sys
import json
#from pprint import pprint

class ApicRestClient(object): 
    """
    A class for communicating with APIC REST API with the SUPPORTED_METHODS below.
    """
    SUPPORTED_METHODS = ['GET', 'POST', 'DELETE']
    http_header={"User-Agent" : "Chrome/17.0.963.46",
            "Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
            "Accept-Language" : "en-us,en;q=0.5",
            "Accept-Charset" : "ISO-8859-1",
            "Content-type": "application/x-www-form-urlencoded"}


    def __init__(self, apic_ip, apic_port, apic_user, apic_password, **kwargs):
        """

        """
        self.apic_ip = apic_ip
        self.apic_port = apic_port
        self.apic_user = apic_user
        self.apic_password = apic_password
        self.verify = kwargs.get('verify', False)
        self.session = requests.Session()
        self.protocol = 'https'
        self.cookie = self.__login()

    def __login(self):
        # __login is called by __init__ only
        loggedIn = self.__getCookie()
        if loggedIn:
            print("APIO Login Successful.")
            return loggedIn
        else:
            print("Failed to login APIC. Please verify credentials.")
            sys.exit(2)
        
    def __getCookie(self):
    
        self.http_header["Host"] = self.apic_ip
        url = '%s://%s:%s/api/aaaLogin.xml' % (self.protocol, self.apic_ip, self.apic_port)
        login_string = '<aaaUser name="%s" pwd="%s"/>' % (self.apic_user, self.apic_password)

        req = requests.post(url, data=login_string, headers=self.http_header, verify=False)
        raw_cookie = req.cookies['APIC-cookie']

        return raw_cookie
        

    def sendApicRequest(self, http_method, uri_path, args=None):
        """

        """
        if http_method not in self.SUPPORTED_METHODS:
            warnings.warn('HTTP method "%s" is unsupported. Returning None' % http_method)
            return None
        
        args = {} if args is None else args
        self.http_header["Host"] = self.apic_ip
        json_body = args.get('json_body', '')
        cookies = {}
        cookies['APIC-cookie'] = self.cookie

        url = "%s://%s:%s%s" %(self.protocol, self.apic_ip, self.apic_port, uri_path)
        unprep_req = requests.Request(http_method, url, headers=self.http_header, cookies=cookies, json=json_body)
        req = self.session.prepare_request(unprep_req)
        return self.session.send(req, verify=self.verify)
        
        

    def get(self, uri_path='', **kwargs):
        """
        """
        return self.sendApicRequest(http_method='GET', uri_path=uri_path, args=kwargs)


    def post(self, uri_path='',**kwargs):
        """
        """
        return self.sendApicRequest(http_method='POST', uri_path=uri_path, args=kwargs)

    def delete(self, uri_path='', **kwargs):
        """
        """
        return self.sendApicRequest(http_method='DELETE', uri_path=uri_path, args=kwargs)

'''

def main():   
    ip = 'localhost' 
    user = 'admin'
    port = '16114'
    password = 'Col1@3col1@3Col'

    #cookie = getAPICCookie(ip, user, password, port)

#   apicurl='/api/node/class/fvBD.json?query-target=subtree&rsp-subtree=full'
    apicurl = '/api/node/mo/uni/tn-ocass.json?query-target=children&target-subtree-class=fvBD&query-target-filter=not(wcard(fvBD.dn,"__ui_"))&rsp-subtree=full&rsp-subtree-class=fvSubnet,fvRsCtx'
    apicurl = '/api/node/mo/uni/tn-ocass.json?query-target=children&target-subtree-class=fvBD&query-target-filter=not(wcard(fvBD.dn,"__ui_"))&rsp-subtree=full&rsp-subtree-class=fvSubnet,fvRsCtx'
    apicurl = '/api/node/class/fvBD.json?query-target=subtree&target-subtree-class=fvBD&rsp-subtree=full&rsp-subtree-class=fvSubnet,fvRsCtx'
    #r = sendAPICRequest(ip,cookie,apicurl,port)

    rc = ApicRestClient(ip,port,user,password)
    #rc.get(apicurl)

    r = rc.get(apicurl).text
    parsed_json = json.loads(r)
    #print(r)
    if r:
        parsed_json = json.loads(r)
    for bd in parsed_json['imdata']:
        bdDN = bd['fvBD']['attributes']['dn']
        bcastP = bd['fvBD']['attributes']['bcastP']
        print("{} uses {}".format(bdDN, bcastP)) 
    else:
        print("That didn't work, we received no response back!")

    print(json.dumps(parsed_json['imdata'][10], indent=4))

if __name__ == '__main__':
    sys.exit(main())

'''