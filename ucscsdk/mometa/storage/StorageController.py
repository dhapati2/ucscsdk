"""This module contains the general information for StorageController ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageControllerConsts():
    ADMIN_ACTION_CLEAR_BOOT_CONFIGURATION = "clear-boot-configuration"
    ADMIN_ACTION_CLEAR_FOREIGN_CONFIGURATION = "clear-foreign-configuration"
    ADMIN_ACTION_DISABLE_SECURITY = "disable-security"
    ADMIN_ACTION_ENABLE_SECURITY = "enable-security"
    ADMIN_ACTION_IMPORT_FOREIGN_CONFIGURATION = "import-foreign-configuration"
    ADMIN_ACTION_MODIFY_KEY = "modify-key"
    ADMIN_ACTION_SKIP_INITIAL_CONFIG = "skip-initial-config"
    ADMIN_ACTION_UNLOCK_DISK = "unlock-disk"
    ADMIN_ACTION_UNPIN_CACHE_ALL = "unpin-cache-all"
    ADMIN_ACTION_UNSPECIFIED = "unspecified"
    ADMIN_ACTION_TRIGGER_CANCELED = "canceled"
    ADMIN_ACTION_TRIGGER_IDLE = "idle"
    ADMIN_ACTION_TRIGGER_TRIGGERED = "triggered"
    CONFIG_STATE_N_A = "N/A"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONFIG_STATE_UNKNOWN = "unknown"
    CONTROLLER_STATUS_DEGRADED = "degraded"
    CONTROLLER_STATUS_FAILED = "failed"
    CONTROLLER_STATUS_OPTIMAL = "optimal"
    CONTROLLER_STATUS_UNKNOWN = "unknown"
    CONTROLLER_STATUS_UNRESPONSIVE = "unresponsive"
    ID_COUNT_MIN = "min"
    ID_COUNT_UNKNOWN = "unknown"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    MODE_AHCI = "AHCI"
    MODE_HBA = "HBA"
    MODE_M2_HWRAID = "M2HWRAID"
    MODE_NVME = "NVME"
    MODE_PHBA = "PHBA"
    MODE_PRAID = "PRAID"
    MODE_RAID = "RAID"
    MODE_SAS4 = "SAS4"
    MODE_SWRAID = "SWRAID"
    MODE_XSDS = "XSDS"
    MODE_UNKNOWN = "unknown"
    ON_BOARD_MEMORY_PRESENT_NO = "no"
    ON_BOARD_MEMORY_PRESENT_UNKNOWN = "unknown"
    ON_BOARD_MEMORY_PRESENT_YES = "yes"
    ON_BOARD_MEMORY_SIZE_UNKNOWN = "unknown"
    OOB_CONTROLLER_ID_NOT_APPLICABLE = "not-applicable"
    OOB_INTERFACE_SUPPORTED_FALSE = "false"
    OOB_INTERFACE_SUPPORTED_NO = "no"
    OOB_INTERFACE_SUPPORTED_TRUE = "true"
    OOB_INTERFACE_SUPPORTED_YES = "yes"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    OPER_STATE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPER_STATE_IDENTIFY = "identify"
    OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MALFORMED_FRU = "malformed-fru"
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    OPER_STATE_POST_FAILURE = "post-failure"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_POWERED_OFF = "powered-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
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
    OPROM_BOOT_STATUS_DISABLED = "disabled"
    OPROM_BOOT_STATUS_ENABLED = "enabled"
    OPROM_BOOT_STATUS_UNKNOWN = "unknown"
    PERF_LOWER_CRITICAL = "lower-critical"
    PERF_LOWER_NON_CRITICAL = "lower-non-critical"
    PERF_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    PERF_NOT_SUPPORTED = "not-supported"
    PERF_OK = "ok"
    PERF_UNKNOWN = "unknown"
    PERF_UPPER_CRITICAL = "upper-critical"
    PERF_UPPER_NON_CRITICAL = "upper-non-critical"
    PERF_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    PINNED_CACHE_STATUS_DISABLED = "disabled"
    PINNED_CACHE_STATUS_ENABLED = "enabled"
    PINNED_CACHE_STATUS_UNKNOWN = "unknown"
    POWER_DEGRADED = "degraded"
    POWER_ERROR = "error"
    POWER_FAILED = "failed"
    POWER_NOT_SUPPORTED = "not-supported"
    POWER_OFF = "off"
    POWER_OFFDUTY = "offduty"
    POWER_OFFLINE = "offline"
    POWER_OK = "ok"
    POWER_ON = "on"
    POWER_ONLINE = "online"
    POWER_POWER_SAVE = "power-save"
    POWER_TEST = "test"
    POWER_UNKNOWN = "unknown"
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
    REBUILD_RATE_NOT_APPLICABLE = "not-applicable"
    REBUILD_RATE_UNKNOWN = "unknown"
    SUB_OEM_ID_UNKNOWN = "unknown"
    SUB_TYPE_NA = "NA"
    SUB_TYPE_NVME_FRONT = "NVME-FRONT"
    SUB_TYPE_NVME_HHHL = "NVME-HHHL"
    SUB_TYPE_NVME_M2 = "NVME-M2"
    SUB_TYPE_NVME_MEZZ = "NVME-MEZZ"
    SUB_TYPE_NVME_REAR = "NVME-REAR"
    SUB_TYPE_RDE = "RDE"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    TYPE_FLASH = "FLASH"
    TYPE_HBA = "HBA"
    TYPE_NVME = "NVME"
    TYPE_PCH = "PCH"
    TYPE_PT = "PT"
    TYPE_SAS = "SAS"
    TYPE_SATA = "SATA"
    TYPE_SD = "SD"
    TYPE_EXTERNAL = "external"
    TYPE_UNKNOWN = "unknown"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class StorageController(ManagedObject):
    """This is StorageController class."""

    consts = StorageControllerConsts()
    naming_props = set(['type', 'id'])

    mo_meta = MoMeta("StorageController", "storageController", "storage-[type]-[id]", VersionMeta.Version111a, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['computeBoard', 'equipmentChassis'], ['faultInst', 'firmwareBootDefinition', 'firmwareRunning', 'lstorageControllerDef', 'mgmtController', 'storageControllerOperation', 'storageEmbeddedStorage', 'storageEnclosure', 'storageLocalDisk', 'storageLocalDiskConfigDef', 'storageLocalDiskEp', 'storageLocalLun', 'storageMezzFlashLife', 'storageNvmeStats', 'storageNvmeStorage', 'storageOnboardDevice', 'storageOperation', 'storageRaidBattery', 'storageSsdHealthStats', 'storageVirtualDrive', 'storageVirtualDriveEp'], ["Get"])

    prop_meta = {
        "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["clear-boot-configuration", "clear-foreign-configuration", "disable-security", "enable-security", "import-foreign-configuration", "modify-key", "skip-initial-config", "unlock-disk", "unpin-cache-all", "unspecified"], []), 
        "admin_action_trigger": MoPropertyMeta("admin_action_trigger", "adminActionTrigger", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["canceled", "idle", "triggered"], []), 
        "admin_security_key": MoPropertyMeta("admin_security_key", "adminSecurityKey", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned", "unknown"], []), 
        "controller_flags": MoPropertyMeta("controller_flags", "controllerFlags", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|driveSecurityCapable|driveSecurityEnable),){0,3}(defaultValue|none|driveSecurityCapable|driveSecurityEnable){0,1}""", [], []), 
        "controller_ops": MoPropertyMeta("controller_ops", "controllerOps", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|unlock-disk|get-phy-errors|ctlr-shutdown|set-suboem|get-foreign-configuration|no-ops-supported|disable-security|clear-all-config|get-pinned-list|set-factory-defaults|clear-foreign-configuration|modify|update-boot-drive|unpin-cache|get-time-secs|import-foreign-configuration|clear-boot-drive|ctlr-lock-operation|set-time-secs|get-suboem|get-tty-log),){0,22}(defaultValue|unknown|unlock-disk|get-phy-errors|ctlr-shutdown|set-suboem|get-foreign-configuration|no-ops-supported|disable-security|clear-all-config|get-pinned-list|set-factory-defaults|clear-foreign-configuration|modify|update-boot-drive|unpin-cache|get-time-secs|import-foreign-configuration|clear-boot-drive|ctlr-lock-operation|set-time-secs|get-suboem|get-tty-log){0,1}""", [], []), 
        "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "failed", "optimal", "unknown", "unresponsive"], []), 
        "default_strip_size": MoPropertyMeta("default_strip_size", "defaultStripSize", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB),){0,19}(defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB){0,1}""", [], []), 
        "device_raid_support": MoPropertyMeta("device_raid_support", "deviceRaidSupport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "disk_ops": MoPropertyMeta("disk_ops", "diskOps", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|clear-secure-foreign-config-drive|set-rebuild-status|clear-foreign-configuration|cancel-rebuild|make-offline|make-ghsp|no-ops-supported|get-phy-errors|set-copyback-status|set-state|get-pd-progress|prepare-to-remove|make-dhsp|remove|smart-ssd-support|enable-security-on-jbod|set-boot-drive|get-foreign-configuration|undo-prepare-to-remove|remove-hsp|locate-start|clear-secure-drive|update-lrop-status|import-foreign-configuration|start-rebuild|make-online|locate-stop),){0,28}(defaultValue|unknown|clear-secure-foreign-config-drive|set-rebuild-status|clear-foreign-configuration|cancel-rebuild|make-offline|make-ghsp|no-ops-supported|get-phy-errors|set-copyback-status|set-state|get-pd-progress|prepare-to-remove|make-dhsp|remove|smart-ssd-support|enable-security-on-jbod|set-boot-drive|get-foreign-configuration|undo-prepare-to-remove|remove-hsp|locate-start|clear-secure-drive|update-lrop-status|import-foreign-configuration|start-rebuild|make-online|locate-stop){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "err_description": MoPropertyMeta("err_description", "errDescription", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 64, None, [], []), 
        "fault_monitoring": MoPropertyMeta("fault_monitoring", "faultMonitoring", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "hw_revision": MoPropertyMeta("hw_revision", "hwRevision", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-64"]), 
        "id_count": MoPropertyMeta("id_count", "idCount", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["min", "unknown"], ["0-4294967295"]), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "location_dn": MoPropertyMeta("location_dn", "locationDn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["AHCI", "HBA", "M2HWRAID", "NVME", "PHBA", "PRAID", "RAID", "SAS4", "SWRAID", "XSDS", "unknown"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "on_board_memory_present": MoPropertyMeta("on_board_memory_present", "onBoardMemoryPresent", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "unknown", "yes"], []), 
        "on_board_memory_size": MoPropertyMeta("on_board_memory_size", "onBoardMemorySize", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "oob_controller_id": MoPropertyMeta("oob_controller_id", "oobControllerId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "oob_interface_supported": MoPropertyMeta("oob_interface_supported", "oobInterfaceSupported", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "oprom_boot_status": MoPropertyMeta("oprom_boot_status", "opromBootStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], []), 
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pci_slot_raw_name": MoPropertyMeta("pci_slot_raw_name", "pciSlotRawName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "pinned_cache_status": MoPropertyMeta("pinned_cache_status", "pinnedCacheStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "raid_battery_ops": MoPropertyMeta("raid_battery_ops", "raidBatteryOps", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|no-ops-supported|disable-learn|enable-learn|start-learn-cycle),){0,5}(defaultValue|unknown|no-ops-supported|disable-learn|enable-learn|start-learn-cycle){0,1}""", [], []), 
        "raid_support": MoPropertyMeta("raid_support", "raidSupport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rebuild_rate": MoPropertyMeta("rebuild_rate", "rebuildRate", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable", "unknown"], ["0-101"]), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sub_oem_id": MoPropertyMeta("sub_oem_id", "subOemId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "sub_type": MoPropertyMeta("sub_type", "subType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "NVME-FRONT", "NVME-HHHL", "NVME-M2", "NVME-MEZZ", "NVME-REAR", "RDE"], []), 
        "supported_strip_sizes": MoPropertyMeta("supported_strip_sizes", "supportedStripSizes", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB),){0,19}(defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB){0,1}""", [], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x100, None, None, None, ["FLASH", "HBA", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "variant_type": MoPropertyMeta("variant_type", "variantType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "virtual_drive_ops": MoPropertyMeta("virtual_drive_ops", "virtualDriveOps", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|set-changed|clear-transport-ready|set-cc-status|get-maxsize|get-reconstruction-info|cancel-initialization|delete-operation|no-ops-supported|get-disk-group|unpin-cache-op|update-lrop-status|get-ld-progress|start-check-consistency|modify-operation|deleted|set-reconstruction-status|secure-drive-group|set-hidden-op|start-patrol-read|cancel-check-consistency|set-boot-drive-operation|create-operation|set-initialization-status|set-transport-ready|clear-hidden-op|stop-patrol-read|start-reconstruction|start-initialization|carve-operation),){0,30}(defaultValue|unknown|set-changed|clear-transport-ready|set-cc-status|get-maxsize|get-reconstruction-info|cancel-initialization|delete-operation|no-ops-supported|get-disk-group|unpin-cache-op|update-lrop-status|get-ld-progress|start-check-consistency|modify-operation|deleted|set-reconstruction-status|secure-drive-group|set-hidden-op|start-patrol-read|cancel-check-consistency|set-boot-drive-operation|create-operation|set-initialization-status|set-transport-ready|clear-hidden-op|stop-patrol-read|start-reconstruction|start-initialization|carve-operation){0,1}""", [], []), 
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
    }

    prop_map = {
        "adminAction": "admin_action", 
        "adminActionTrigger": "admin_action_trigger", 
        "adminSecurityKey": "admin_security_key", 
        "assetTag": "asset_tag", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "controllerFlags": "controller_flags", 
        "controllerOps": "controller_ops", 
        "controllerStatus": "controller_status", 
        "defaultStripSize": "default_strip_size", 
        "deviceRaidSupport": "device_raid_support", 
        "diskOps": "disk_ops", 
        "dn": "dn", 
        "errDescription": "err_description", 
        "faultMonitoring": "fault_monitoring", 
        "hwRevision": "hw_revision", 
        "id": "id", 
        "idCount": "id_count", 
        "lc": "lc", 
        "locationDn": "location_dn", 
        "mode": "mode", 
        "model": "model", 
        "onBoardMemoryPresent": "on_board_memory_present", 
        "onBoardMemorySize": "on_board_memory_size", 
        "oobControllerId": "oob_controller_id", 
        "oobInterfaceSupported": "oob_interface_supported", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "opromBootStatus": "oprom_boot_status", 
        "partNumber": "part_number", 
        "pciAddr": "pci_addr", 
        "pciSlot": "pci_slot", 
        "pciSlotRawName": "pci_slot_raw_name", 
        "perf": "perf", 
        "pinnedCacheStatus": "pinned_cache_status", 
        "power": "power", 
        "presence": "presence", 
        "raidBatteryOps": "raid_battery_ops", 
        "raidSupport": "raid_support", 
        "rebuildRate": "rebuild_rate", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "subOemId": "sub_oem_id", 
        "subType": "sub_type", 
        "supportedStripSizes": "supported_strip_sizes", 
        "thermal": "thermal", 
        "type": "type", 
        "variantType": "variant_type", 
        "vendor": "vendor", 
        "vid": "vid", 
        "virtualDriveOps": "virtual_drive_ops", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, type, id, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.id = id
        self.admin_action = None
        self.admin_action_trigger = None
        self.admin_security_key = None
        self.asset_tag = None
        self.child_action = None
        self.config_state = None
        self.controller_flags = None
        self.controller_ops = None
        self.controller_status = None
        self.default_strip_size = None
        self.device_raid_support = None
        self.disk_ops = None
        self.err_description = None
        self.fault_monitoring = None
        self.hw_revision = None
        self.id_count = None
        self.lc = None
        self.location_dn = None
        self.mode = None
        self.model = None
        self.on_board_memory_present = None
        self.on_board_memory_size = None
        self.oob_controller_id = None
        self.oob_interface_supported = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.oprom_boot_status = None
        self.part_number = None
        self.pci_addr = None
        self.pci_slot = None
        self.pci_slot_raw_name = None
        self.perf = None
        self.pinned_cache_status = None
        self.power = None
        self.presence = None
        self.raid_battery_ops = None
        self.raid_support = None
        self.rebuild_rate = None
        self.revision = None
        self.serial = None
        self.status = None
        self.sub_oem_id = None
        self.sub_type = None
        self.supported_strip_sizes = None
        self.thermal = None
        self.variant_type = None
        self.vendor = None
        self.vid = None
        self.virtual_drive_ops = None
        self.voltage = None

        ManagedObject.__init__(self, "StorageController", parent_mo_or_dn, **kwargs)

