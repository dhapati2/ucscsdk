"""This module contains the general information for FaultPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FaultPolicyConsts():
    ACK_ACTION_DELETE_ON_CLEAR = "delete-on-clear"
    ACK_ACTION_INITIAL_SEVERITY = "initial-severity"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CLEAR_ACTION_DELETE = "delete"
    CLEAR_ACTION_RETAIN = "retain"
    CLEAR_INTERVAL_NEVER = "never"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    RETENTION_INTERVAL_FOREVER = "forever"
    SIZE_LIMIT_MAX = "max"
    SOAK_INTERVAL_NEVER = "never"
    SOAKING_SEVERITY_CONDITION = "condition"
    SOAKING_SEVERITY_INFO = "info"
    SOAKING_SEVERITY_WARNING = "warning"


class FaultPolicy(ManagedObject):
    """This is FaultPolicy class."""

    consts = FaultPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("FaultPolicy", "faultPolicy", "fault-policy", VersionMeta.Version101a, "InputOutput", 0x7fff, [], ["admin", "fault"], ['orgDomainGroup', 'orgOrg', 'policyDeviceProfile'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "ack_action": MoPropertyMeta("ack_action", "ackAction", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["delete-on-clear", "initial-severity"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clear_action": MoPropertyMeta("clear_action", "clearAction", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["delete", "retain"], []), 
        "clear_interval": MoPropertyMeta("clear_interval", "clearInterval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["never"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "flap_interval": MoPropertyMeta("flap_interval", "flapInterval", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["5-3600"]), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "retention_interval": MoPropertyMeta("retention_interval", "retentionInterval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["forever"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "size_limit": MoPropertyMeta("size_limit", "sizeLimit", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["max"], ["0-20000"]), 
        "soak_interval": MoPropertyMeta("soak_interval", "soakInterval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["never"], ["0-3600"]), 
        "soaking_severity": MoPropertyMeta("soaking_severity", "soakingSeverity", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["condition", "info", "warning"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "ackAction": "ack_action", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "clearAction": "clear_action", 
        "clearInterval": "clear_interval", 
        "descr": "descr", 
        "dn": "dn", 
        "flapInterval": "flap_interval", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "retentionInterval": "retention_interval", 
        "rn": "rn", 
        "sizeLimit": "size_limit", 
        "soakInterval": "soak_interval", 
        "soakingSeverity": "soaking_severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ack_action = None
        self.admin_state = None
        self.child_action = None
        self.clear_action = None
        self.clear_interval = None
        self.descr = None
        self.flap_interval = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.retention_interval = None
        self.size_limit = None
        self.soak_interval = None
        self.soaking_severity = None
        self.status = None

        ManagedObject.__init__(self, "FaultPolicy", parent_mo_or_dn, **kwargs)

