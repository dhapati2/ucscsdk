"""This module contains the general information for CommSmashCLP ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CommSmashCLPConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommSmashCLP(ManagedObject):
    """This is CommSmashCLP class."""

    consts = CommSmashCLPConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommSmashCLP", "commSmashCLP", "smashclp-svc", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["aaa", "admin"], ['orgDomainGroup', 'orgOrg'], [], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_port": MoPropertyMeta("oper_port", "operPort", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-65535"]), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operPort": "oper_port", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "port": "port", 
        "proto": "proto", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.oper_port = None
        self.policy_level = None
        self.policy_owner = None
        self.port = None
        self.proto = None
        self.status = None

        ManagedObject.__init__(self, "CommSmashCLP", parent_mo_or_dn, **kwargs)

