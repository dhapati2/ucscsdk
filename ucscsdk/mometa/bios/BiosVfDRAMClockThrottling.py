"""This module contains the general information for BiosVfDRAMClockThrottling ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfDRAMClockThrottlingConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_DRAMCLOCK_THROTTLING_AUTO = "auto"
    VP_DRAMCLOCK_THROTTLING_BALANCED = "balanced"
    VP_DRAMCLOCK_THROTTLING_ENERGY_EFFICIENT = "energy-efficient"
    VP_DRAMCLOCK_THROTTLING_PERFORMANCE = "performance"
    VP_DRAMCLOCK_THROTTLING_PLATFORM_DEFAULT = "platform-default"
    VP_DRAMCLOCK_THROTTLING_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfDRAMClockThrottling(ManagedObject):
    """This is BiosVfDRAMClockThrottling class."""

    consts = BiosVfDRAMClockThrottlingConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfDRAMClockThrottling", "biosVfDRAMClockThrottling", "DRAM-Clock-Throttling", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_dram_clock_throttling": MoPropertyMeta("vp_dram_clock_throttling", "vpDRAMClockThrottling", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "balanced", "energy-efficient", "performance", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpDRAMClockThrottling": "vp_dram_clock_throttling", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_dram_clock_throttling = None

        ManagedObject.__init__(self, "BiosVfDRAMClockThrottling", parent_mo_or_dn, **kwargs)

