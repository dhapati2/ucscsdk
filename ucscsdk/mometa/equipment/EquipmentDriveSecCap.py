"""This module contains the general information for EquipmentDriveSecCap ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentDriveSecCapConsts():
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class EquipmentDriveSecCap(ManagedObject):
    """This is EquipmentDriveSecCap class."""

    consts = EquipmentDriveSecCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentDriveSecCap", "equipmentDriveSecCap", "drive-sec-cap", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentRackUnitCapProvider'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "min_version": MoPropertyMeta("min_version", "minVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSupported": "is_supported", 
        "minVersion": "min_version", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_supported = None
        self.min_version = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentDriveSecCap", parent_mo_or_dn, **kwargs)

