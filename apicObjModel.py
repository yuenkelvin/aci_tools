#!/usr/bin/env python3

import json
import sys
import apic
import urllib3

class ApicObjModel(object):
    """
    A class to work with objects in the Apic Module
    """

    def __init__(self, rc:apic.ApicRestClient , uri_path):
        """
            rc : Apic Rest Client to conduct the call 
            uri_path : url path to retrieve the object e.g. (/api/node/class/... or /api/node/mo/...)
            raw : full data under imdata untouched
        """
        self.rc = rc
        self.uri_path = uri_path
        self.raw = self.getAll()

    def getAll(self, raw=False):
        """
        """
        r = self.rc.get(self.uri_path).text
        parsed_json = json.loads(r)
        if raw == False: 
            return [ parsed_json['imdata'][x][y] for x in range(len(parsed_json['imdata'])) for y in parsed_json['imdata'][x] ]
        else :
            return parsed_json['imdata']

    def get(self):
        """
        """
        pass

    def getItem(self, item):
        """
        """
        return self.raw[item]

    def update(self):
        """
        """
        pass

    def delete(self):
        """
        """
        pass
