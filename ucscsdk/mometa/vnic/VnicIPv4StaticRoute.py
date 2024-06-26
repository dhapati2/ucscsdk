"""This module contains the general information for VnicIPv4StaticRoute ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicIPv4StaticRouteConsts():
    pass


class VnicIPv4StaticRoute(ManagedObject):
    """This is VnicIPv4StaticRoute class."""

    consts = VnicIPv4StaticRouteConsts()
    naming_props = set(['addr'])

    mo_meta = MoMeta("VnicIPv4StaticRoute", "vnicIPv4StaticRoute", "ipv4-route-[addr]", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], ['vnicIPv4If'], [], ["Get"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "gw_addr": MoPropertyMeta("gw_addr", "gwAddr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "gw_subnet": MoPropertyMeta("gw_subnet", "gwSubnet", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version111a, MoPropertyMeta.CREATE_ONLY, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "gwAddr": "gw_addr", 
        "gwSubnet": "gw_subnet", 
        "rn": "rn", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, addr, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.child_action = None
        self.def_gw = None
        self.gw_addr = None
        self.gw_subnet = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "VnicIPv4StaticRoute", parent_mo_or_dn, **kwargs)

