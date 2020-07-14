#!/usr/bin/env python3

import requests
import sys
import json
from pprint import pprint


http_header={"User-Agent" : "Chrome/17.0.963.46",
             "Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
             "Accept-Language" : "en-us,en;q=0.5",
             "Accept-Charset" : "ISO-8859-1",
             "Content-type": "application/x-www-form-urlencoded"
            }


def getAPICCookie(ip_addr, username, password, port):
    url = 'https://'+ip_addr+':'+port+'/api/aaaLogin.xml'

    http_header["Host"]=ip_addr
    xml_string = "<aaaUser name='%s' pwd='%s'/>" % (username, password)
    req = requests.post(url, data=xml_string, headers=http_header, verify=False)
    rawcookie=req.cookies['APIC-cookie']
    #print("Rawcookie: {}".format(rawcookie)) 
    return rawcookie

 
def sendAPICRequest(ip_addr, cookie, apicurl, port):
    url = 'https://'+ip_addr+':'+port+apicurl
    http_header["Host"]=ip_addr
    cookies = {} 
    cookies['APIC-cookie'] = cookie
    #cookies['APIC-cookie'] = cookie
    #req = requests.get(url,headers=http_header,cookies=cookies)
    req = requests.get(url,headers=http_header, cookies=cookies, verify=False)
    print("req.text = %s" % (req.text)) 
    return req.text


def main():   
    ip = 'localhost' 
    user = 'admin'
    port = '16114'
    password = 'Col1@3col1@3Col'

    cookie = getAPICCookie(ip, user, password, port)

    apicurl='/api/node/class/fvBD.json'
    r = sendAPICRequest(ip,cookie,apicurl,port)

    #print(r)
    if r:
        parsed_json = json.loads(r)
    for bd in parsed_json['imdata']:
        bdDN = bd['fvBD']['attributes']['dn']
        bcastP = bd['fvBD']['attributes']['bcastP']
        print("{} uses {}".format(bdDN, bcastP)) 
    else:
        print("That didn't work, we received no response back!")


if __name__ == '__main__':
    sys.exit(main())

