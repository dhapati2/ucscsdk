"""This module contains the general information for StorageEnclosureLocalDiskConfig ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageEnclosureLocalDiskConfigConsts():
    BLOCK_SIZE_512 = "512"
    BLOCK_SIZE_UNKNOWN = "unknown"
    CONNECTION_PROTOCOL_NVME = "NVME"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    DEVICE_TYPE_HDD = "HDD"
    DEVICE_TYPE_NVME = "NVME"
    DEVICE_TYPE_SSD = "SSD"
    DEVICE_TYPE_UNSPECIFIED = "unspecified"
    LINK_SPEED_1_5_GBPS = "1-5-gbps"
    LINK_SPEED_12_GBPS = "12-gbps"
    LINK_SPEED_16_GTPS = "16-gtps"
    LINK_SPEED_2_5_GTPS = "2-5-gtps"
    LINK_SPEED_24_GBPS = "24-gbps"
    LINK_SPEED_3_GBPS = "3-gbps"
    LINK_SPEED_5_GTPS = "5-gtps"
    LINK_SPEED_6_GBPS = "6-gbps"
    LINK_SPEED_8_GTPS = "8-gtps"
    LINK_SPEED_NA = "NA"
    LINK_SPEED_DISABLED = "disabled"
    LINK_SPEED_DOWN = "down"
    LINK_SPEED_HOST_POWER_OFF = "host-power-off"
    LINK_SPEED_UNKNOWN = "unknown"
    LINK_SPEED_UNSUPPORTED_DEVICE = "unsupported-device"
    LINK_STATE_MISCONNECT = "misconnect"
    LINK_STATE_OPTIMAL = "optimal"
    LINK_STATE_SUB_OPTIMAL = "sub-optimal"
    LINK_STATE_UNKNOWN = "unknown"
    NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
    OPERABILITY_DISABLED = "disabled"
    OPERABILITY_DISCOVERY = "discovery"
    OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPERABILITY_IDENTIFY = "identify"
    OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_MALFORMED_FRU = "malformed-fru"
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    PHYSICAL_BLOCK_SIZE_512 = "512"
    PHYSICAL_BLOCK_SIZE_UNKNOWN = "unknown"
    POWER_STATE_NA = "NA"
    POWER_STATE_ACTIVE = "active"
    POWER_STATE_OFF = "off"
    POWER_STATE_POWERSAVE = "powersave"
    POWER_STATE_TRANSITIONING = "transitioning"
    POWER_STATE_UNKNOWN = "unknown"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    SCSI_DISK_STATE_BAD = "bad"
    SCSI_DISK_STATE_GOOD = "good"
    SCSI_DISK_STATE_UNKNOWN = "unknown"
    SIZE_NOT_APPLICABLE = "not-applicable"


class StorageEnclosureLocalDiskConfig(ManagedObject):
    """This is StorageEnclosureLocalDiskConfig class."""

    consts = StorageEnclosureLocalDiskConfigConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageEnclosureLocalDiskConfig", "storageEnclosureLocalDiskConfig", "enc-disk-config-[id]", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["read-only"], [], ['storageSasPort'], ["Get"])

    prop_meta = {
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NVME", "SAS", "SATA", "unspecified"], []), 
        "device_type": MoPropertyMeta("device_type", "deviceType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["HDD", "NVME", "SSD", "unspecified"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1-5-gbps", "12-gbps", "16-gtps", "2-5-gtps", "24-gbps", "3-gbps", "5-gtps", "6-gbps", "8-gtps", "NA", "disabled", "down", "host-power-off", "unknown", "unsupported-device"], []), 
        "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["misconnect", "optimal", "sub-optimal", "unknown"], []), 
        "link_state_reason": MoPropertyMeta("link_state_reason", "linkStateReason", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "physical_block_size": MoPropertyMeta("physical_block_size", "physicalBlockSize", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]), 
        "power_state": MoPropertyMeta("power_state", "powerState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "active", "off", "powersave", "transitioning", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "scsi_disk_state": MoPropertyMeta("scsi_disk_state", "scsiDiskState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bad", "good", "unknown"], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "blockSize": "block_size", 
        "childAction": "child_action", 
        "connectionProtocol": "connection_protocol", 
        "deviceType": "device_type", 
        "dn": "dn", 
        "firmwareVersion": "firmware_version", 
        "id": "id", 
        "linkSpeed": "link_speed", 
        "linkState": "link_state", 
        "linkStateReason": "link_state_reason", 
        "model": "model", 
        "numberOfBlocks": "number_of_blocks", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "physicalBlockSize": "physical_block_size", 
        "powerState": "power_state", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "scsiDiskState": "scsi_disk_state", 
        "serial": "serial", 
        "size": "size", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.block_size = None
        self.child_action = None
        self.connection_protocol = None
        self.device_type = None
        self.firmware_version = None
        self.link_speed = None
        self.link_state = None
        self.link_state_reason = None
        self.model = None
        self.number_of_blocks = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.physical_block_size = None
        self.power_state = None
        self.presence = None
        self.revision = None
        self.scsi_disk_state = None
        self.serial = None
        self.size = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageEnclosureLocalDiskConfig", parent_mo_or_dn, **kwargs)

