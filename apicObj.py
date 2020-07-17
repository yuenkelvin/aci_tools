#!/usr/bin/env python3

import json
import sys
import urllib3
import apic
from apicObjModel import ApicObjModel

class fvTenant(ApicObjModel):
    # Tenant
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/fvTenant.json?rsp-subtree-include=health,required&rsp-prop-include=config-only'
        self.rc = rc
        super(fvTenant, self).__init__(rc, self.uri_path)

class fvAEPg(ApicObjModel):
    # EPG
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/fvAEPg.json?query-target=subtree&target-subtree-class=fvAEPg&rsp-subtree=full'
        self.rc = rc 
        super(fvAEPg, self).__init__(rc, self.uri_path)

class fvCtx(ApicObjModel):
    # VRF
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/fvCtx.json?query-target=subtree&target-subtree-class=fvCtx'
        self.rc = rc
        super(fvCtx, self).__init__(rc, self.uri_path)

class fvBD(ApicObjModel):
    # BD
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/fvBD.json?query-target=subtree&target-subtree-class=fvBD&rsp-subtree=full&rsp-subtree-class=fvSubnet,fvRsCtx'
        self.rc = rc
        super(fvBD,self).__init__(rc, self.uri_path)


class dhcpClient(ApicObjModel):
    #Fabric Membership
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/dhcpClient.json?query-target-filter=or(eq(dhcpClient.nodeRole,%22leaf%22),eq(dhcpClient.nodeRole,%22spine%22),eq(dhcpClient.nodeRole,%22unsupported%22))'
        self.rc = rc
        super(dhcpClient,self).__init__(rc, self.uri_path)

class maintMaintGrp(ApicObjModel):
    #Maintenance Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/fabric/maintgrp-Spine.json?rsp-subtree=full&rsp-subtree-include=relations&challenge=null'
        self.uri_path = '/api/node/class/maintMaintGrp.json?query-target=subtree&target-subtree-class=maintMaintGrp&rsp-subtree=full'
        self.rc = rc
        super(maintMaintGrp,self).__init__(rc, self.uri_path)

class maintMaintP(ApicObjModel):
    #Upgrade Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/maintMaintP.json?query-target=subtree&target-subtree-class=maintMaintP&rsp-subtree=full'
        self.rc = rc
        super(maintMaintP, self).__init__(rc, self.uri_path)

class bgpInstP(ApicObjModel):
    #bgp
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/fabric/bgpInstP-default.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(bgpInstP, self).__init__(rc, self.uri_path)

class latencyPtpMode(ApicObjModel):
    #PTP   
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/fabric/ptpmode.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(latencyPtpMode, self).__init__(rc, self.uri_path)

class datetimeFormat(ApicObjModel):
    #datetime
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/fabric/format-default.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(datetimeFormat, self).__init__(rc, self.uri_path)

class infraPortTrackPol(ApicObjModel):
    #Port Tracking
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/infra/trackEqptFabP-default.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(infraPortTrackPol,self).__init__(rc, self.uri_path)

class infraSetPol(ApicObjModel):
    #Infra-wide Settings
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/infra/settings.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(infraSetPol, self).__init__(rc, self.uri_path)

class fabricPodP(ApicObjModel):
    #Fabric Pod Profile <--- to be investigate. 
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/fabric.json?query-target=subtree&target-subtree-class=fabricPodP&rsp-subtree=full'
        self.rc = rc
        super(fabricPodP,self).__init__(rc, self.uri_path)

class fabricPodPGrp(ApicObjModel):
    #Fabric Pod Policy Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/fabric/funcprof.json?query-target=subtree&target-subtree-class=fabricPodPGrp&query-target-filter=not(wcard(fabricPodPGrp.dn,%22__ui_%22))&target-subtree-class=fabricRsTimePol,fabricRsPodPGrpBGPRRP,fabricRsPodPGrpIsisDomP,fabricRsPodPGrpCoopP,fabricRsCommPol,fabricRsSnmpPol&query-target=subtree'
        self.rc = rc
        super(fabricPodPGrp, self).__init__(rc, self.uri_path)

class datetimePol(ApicObjModel):
    #NTP
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/datetimePol.json?query-target-filter=not(wcard(datetimePol.dn,%22__ui_%22))&rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(datetimePol, self).__init__(rc,self.uri_path)

class snmpPol(ApicObjModel):
    #SNMP
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/snmpPol.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(snmpPol,self).__init__(rc,self.uri_path)


class fvnsVlanInstP(ApicObjModel):
    #Fabric VLAN Pool
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=subtree&target-subtree-class=fvnsVlanInstP&rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(fvnsVlanInstP,self).__init__(rc, self.uri_path)


class physDomP(ApicObjModel):
    #Fabric Physical Domain
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni.json?query-target=subtree&target-subtree-class=physDomP&rsp-prop-include=config-only'
        self.rc = rc
        super(physDomP,self).__init__(rc, self.uri_path)


class l3extDomP(ApicObjModel):
    #Fabric L3 Domain
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni.json?query-target=subtree&target-subtree-class=l3extDomP&query-target=subtree&rsp-prop-include=config-only'
        self.rc = rc
        super(l3extDomP,self).__init__(rc, self.uri_path)


class infraAttEntityP(ApicObjModel):
    #AAEP
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=subtree&target-subtree-class=infraAttEntityP&query-target=subtree&rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(infraAttEntityP, self).__init__(rc,self.uri_path)

class qosinst(ApicObjModel):
    #QoS Class
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/infra/qosinst-default.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(qosinst, self).__init__(rc,self.uri_path)

class edrErrDisRecoverPol(ApicObjModel):
    #Error Disable Recovery Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/infra/edrErrDisRecoverPol-default.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(edrErrDisRecoverPol,self).__init__(rc, self.uri_path)


class protpol(ApicObjModel):
    #vpc protection policy 
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/mo/uni/fabric/protpol.json?rsp-subtree=full&rsp-prop-include=config-only'
        self.rc = rc
        super(protpol, self).__init__(rc, self.uri_path)



class fabricHIfPol(ApicObjModel):
    #Switch Interface Link Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/fabricHIfPol.json'
        self.rc = rc
        super(fabricHIfPol, self).__init__(rc, self.uri_path)


class cdpIfPol(ApicObjModel):
    #CDP Interface Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/cdpIfPol.json?'
        self.rc = rc
        super(cdpIfPol, self).__init__(rc, self.uri_path)

class lldpIfPol(ApicObjModel):
    #LLDP Interface Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=lldpIfPol'
        self.rc = rc
        super(lldpIfPol, self).__init__(rc,self.uri_path)

class lacpLagPol(ApicObjModel):
    #LACP Lag Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=lacpLagPol'
        self.rc = rc
        super(lacpLagPol,self).__init__(rc,self.uri_path)

class mcpIfPol(ApicObjModel):
    #MCP Interface Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=mcpIfPol'
        self.rc = rc
        super(mcpIfPol,self).__init__(rc,self.uri_path)

    
class stpIfPol(ApicObjModel):
    #Spanning-tree Interface Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/stpIfPol.json'
        self.rc = rc
        super(stpIfPol,self).__init__(rc,self.uri_path)

class stormctrlIfPol(ApicObjModel):
    #Storm Control Interface Policy
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=stormctrlIfPol'
        self.rc = rc
        super(stormctrlIfPol,self).__init__(rc,self.uri_path)

class infraNodeP(ApicObjModel):
    #Leaf Switch Access Profile
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=infraNodeP&rsp-subtree=full&rsp-subtree-class=infraLeafS,infraRsAccPortP,infraRsAccCardP,infraNodeBlk,infraRsAccNodePGrp'
        self.rc = rc
        super(infraNodeP, self).__init__(rc,self.uri_path)

class infraAccNodePGrp(ApicObjModel):
    #Leaf Switch Access Policy Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra/funcprof.json?query-target=subtree&target-subtree-class=infraAccNodePGrp&rsp-subtree=full'
        self.rc = rc
        super(infraAccNodePGrp,self).__init__(rc,self.uri_path)


class infraSpineP(ApicObjModel):
    #Spine Switch Access Profile
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path= '/api/node/mo/uni/infra.json?query-target=subtree&target-subtree-class=infraSpineP&rsp-subtree=full&rsp-subtree-class=infraSpineS,infraNodeBlk,infraRsSpineAccNodePGrp'
        self.rc = rc
        super(infraSpineP, self).__init__(rc,self.uri_path)

class infraSpineAccNodePGrp(ApicObjModel):
    #Spine Switch Policy Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra/funcprof.json?query-target=subtree&target-subtree-class=infraSpineAccNodePGrp&rsp-subtree=full'
        self.rc = rc
        super(infraSpineAccNodePGrp, self).__init__(rc,self.uri_path)

class infraAccPortP(ApicObjModel):
    #Leaf Switch Acess Port Profile
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=subtree&target-subtree-class=infraAccPortP&rsp-subtree=full'
        self.rc = rc
        super(infraAccPortP, self).__init__(rc, self.uri_path)


class infraAccPortGrp(ApicObjModel):
    #Leaf Switch Access Port Access Policy Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra/funcprof.json?query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=full'
        self.rc = rc
        super(infraAccPortGrp,self).__init__(rc, self.uri_path)


class infraAccBndlGrp(ApicObjModel):
    #Leaf Switch vPC/PC Access Policy Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra/funcprof.json?query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=full'
        self.rc = rc
        super(infraAccBndlGrp, self).__init__(rc, self.uri_path)


class infraSpAccPortP(ApicObjModel):
    #Spine Access Port Profile
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=infraSpAccPortP&rsp-subtree=full'
        self.rc = rc
        super(infraSpAccPortP, self).__init__(rc, self.uri_path)


class infraSpAccPortGrp(ApicObjModel):
    #Spine Access Port Policy Group
    def __init__(self, rc:apic.ApicRestClient):
        self.uri_path = '/api/node/class/infraSpAccPortGrp.json?rsp-subtree=full'
        self.rc = rc
        super(infraSpAccPortGrp, self).__init__(rc, self.uri_path)

    



