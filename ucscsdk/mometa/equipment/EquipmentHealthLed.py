"""This module contains the general information for EquipmentHealthLed ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentHealthLedConsts():
    COLOR_AMBER = "amber"
    COLOR_BLUE = "blue"
    COLOR_GREEN = "green"
    COLOR_RED = "red"
    COLOR_UNKNOWN = "unknown"
    HEALTH_LED_STATE_CRITICAL = "critical"
    HEALTH_LED_STATE_MAJOR = "major"
    HEALTH_LED_STATE_NORMAL = "normal"
    OPER_STATE_BLINKING = "blinking"
    OPER_STATE_ETH = "eth"
    OPER_STATE_FC = "fc"
    OPER_STATE_OFF = "off"
    OPER_STATE_ON = "on"
    OPER_STATE_UNKNOWN = "unknown"


class EquipmentHealthLed(ManagedObject):
    """This is EquipmentHealthLed class."""

    consts = EquipmentHealthLedConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentHealthLed", "equipmentHealthLed", "health-led", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeExtBoard', 'computeRackUnit', 'computeServerUnit', 'equipmentChassis', 'equipmentFanModule', 'equipmentFex', 'equipmentIOCard', 'equipmentPsu'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "color": MoPropertyMeta("color", "color", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "health_led_state": MoPropertyMeta("health_led_state", "healthLedState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["critical", "major", "normal"], []), 
        "health_led_state_qualifier": MoPropertyMeta("health_led_state_qualifier", "healthLedStateQualifier", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "color": "color", 
        "dn": "dn", 
        "healthLedState": "health_led_state", 
        "healthLedStateQualifier": "health_led_state_qualifier", 
        "id": "id", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.color = None
        self.health_led_state = None
        self.health_led_state_qualifier = None
        self.id = None
        self.name = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentHealthLed", parent_mo_or_dn, **kwargs)

