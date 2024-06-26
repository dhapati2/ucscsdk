"""This module contains the general information for CimcvmediaExtMgmtRuleEntry ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CimcvmediaExtMgmtRuleEntryConsts():
    MOUNT_PROTOCOL_CIFS = "cifs"
    MOUNT_PROTOCOL_HTTP = "http"
    MOUNT_PROTOCOL_HTTPS = "https"
    MOUNT_PROTOCOL_NFS = "nfs"
    MOUNT_PROTOCOL_UNKNOWN = "unknown"


class CimcvmediaExtMgmtRuleEntry(ManagedObject):
    """This is CimcvmediaExtMgmtRuleEntry class."""

    consts = CimcvmediaExtMgmtRuleEntryConsts()
    naming_props = set(['mappingName'])

    mo_meta = MoMeta("CimcvmediaExtMgmtRuleEntry", "cimcvmediaExtMgmtRuleEntry", "ext-mgmt-rule-[mapping_name]", VersionMeta.Version121e, "InputOutput", 0x1f, [], ["read-only"], ['cimcvmediaActualMountList'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121e, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ext_mgmt_ip_addr": MoPropertyMeta("ext_mgmt_ip_addr", "extMgmtIpAddr", "string", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "mapping_name": MoPropertyMeta("mapping_name", "mappingName", "string", VersionMeta.Version121e, MoPropertyMeta.NAMING, 0x4, None, None, r"""[a-zA-Z0-9][a-zA-Z0-9_.:-]{0,63}""", [], []), 
        "mgmt_if_ip_addr": MoPropertyMeta("mgmt_if_ip_addr", "mgmtIfIpAddr", "string", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "mount_protocol": MoPropertyMeta("mount_protocol", "mountProtocol", "string", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cifs", "http", "https", "nfs", "unknown"], []), 
        "remote_ip_addr": MoPropertyMeta("remote_ip_addr", "remoteIpAddr", "string", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "remote_port": MoPropertyMeta("remote_port", "remotePort", "uint", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "extMgmtIpAddr": "ext_mgmt_ip_addr", 
        "mappingName": "mapping_name", 
        "mgmtIfIpAddr": "mgmt_if_ip_addr", 
        "mountProtocol": "mount_protocol", 
        "remoteIpAddr": "remote_ip_addr", 
        "remotePort": "remote_port", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, mapping_name, **kwargs):
        self._dirty_mask = 0
        self.mapping_name = mapping_name
        self.child_action = None
        self.ext_mgmt_ip_addr = None
        self.mgmt_if_ip_addr = None
        self.mount_protocol = None
        self.remote_ip_addr = None
        self.remote_port = None
        self.status = None

        ManagedObject.__init__(self, "CimcvmediaExtMgmtRuleEntry", parent_mo_or_dn, **kwargs)

