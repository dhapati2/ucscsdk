"""This module contains the general information for EtherFcoeInterfaceStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EtherFcoeInterfaceStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EtherFcoeInterfaceStatsHist(ManagedObject):
    """This is EtherFcoeInterfaceStatsHist class."""

    consts = EtherFcoeInterfaceStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EtherFcoeInterfaceStatsHist", "etherFcoeInterfaceStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['etherFcoeInterfaceStats'], [], [None])

    prop_meta = {
        "bytes_rx": MoPropertyMeta("bytes_rx", "bytesRx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_rx_delta": MoPropertyMeta("bytes_rx_delta", "bytesRxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_rx_delta_avg": MoPropertyMeta("bytes_rx_delta_avg", "bytesRxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_rx_delta_max": MoPropertyMeta("bytes_rx_delta_max", "bytesRxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_rx_delta_min": MoPropertyMeta("bytes_rx_delta_min", "bytesRxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_tx": MoPropertyMeta("bytes_tx", "bytesTx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_tx_delta": MoPropertyMeta("bytes_tx_delta", "bytesTxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_tx_delta_avg": MoPropertyMeta("bytes_tx_delta_avg", "bytesTxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_tx_delta_max": MoPropertyMeta("bytes_tx_delta_max", "bytesTxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "bytes_tx_delta_min": MoPropertyMeta("bytes_tx_delta_min", "bytesTxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "dropped_rx": MoPropertyMeta("dropped_rx", "droppedRx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_rx_delta": MoPropertyMeta("dropped_rx_delta", "droppedRxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_rx_delta_avg": MoPropertyMeta("dropped_rx_delta_avg", "droppedRxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_rx_delta_max": MoPropertyMeta("dropped_rx_delta_max", "droppedRxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_rx_delta_min": MoPropertyMeta("dropped_rx_delta_min", "droppedRxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_tx": MoPropertyMeta("dropped_tx", "droppedTx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_tx_delta": MoPropertyMeta("dropped_tx_delta", "droppedTxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_tx_delta_avg": MoPropertyMeta("dropped_tx_delta_avg", "droppedTxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_tx_delta_max": MoPropertyMeta("dropped_tx_delta_max", "droppedTxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dropped_tx_delta_min": MoPropertyMeta("dropped_tx_delta_min", "droppedTxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_rx": MoPropertyMeta("errors_rx", "errorsRx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_rx_delta": MoPropertyMeta("errors_rx_delta", "errorsRxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_rx_delta_avg": MoPropertyMeta("errors_rx_delta_avg", "errorsRxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_rx_delta_max": MoPropertyMeta("errors_rx_delta_max", "errorsRxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_rx_delta_min": MoPropertyMeta("errors_rx_delta_min", "errorsRxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_tx": MoPropertyMeta("errors_tx", "errorsTx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_tx_delta": MoPropertyMeta("errors_tx_delta", "errorsTxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_tx_delta_avg": MoPropertyMeta("errors_tx_delta_avg", "errorsTxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_tx_delta_max": MoPropertyMeta("errors_tx_delta_max", "errorsTxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "errors_tx_delta_min": MoPropertyMeta("errors_tx_delta_min", "errorsTxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "packets_rx": MoPropertyMeta("packets_rx", "packetsRx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_rx_delta": MoPropertyMeta("packets_rx_delta", "packetsRxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_rx_delta_avg": MoPropertyMeta("packets_rx_delta_avg", "packetsRxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_rx_delta_max": MoPropertyMeta("packets_rx_delta_max", "packetsRxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_rx_delta_min": MoPropertyMeta("packets_rx_delta_min", "packetsRxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_tx": MoPropertyMeta("packets_tx", "packetsTx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_tx_delta": MoPropertyMeta("packets_tx_delta", "packetsTxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_tx_delta_avg": MoPropertyMeta("packets_tx_delta_avg", "packetsTxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_tx_delta_max": MoPropertyMeta("packets_tx_delta_max", "packetsTxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "packets_tx_delta_min": MoPropertyMeta("packets_tx_delta_min", "packetsTxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "bytesRx": "bytes_rx", 
        "bytesRxDelta": "bytes_rx_delta", 
        "bytesRxDeltaAvg": "bytes_rx_delta_avg", 
        "bytesRxDeltaMax": "bytes_rx_delta_max", 
        "bytesRxDeltaMin": "bytes_rx_delta_min", 
        "bytesTx": "bytes_tx", 
        "bytesTxDelta": "bytes_tx_delta", 
        "bytesTxDeltaAvg": "bytes_tx_delta_avg", 
        "bytesTxDeltaMax": "bytes_tx_delta_max", 
        "bytesTxDeltaMin": "bytes_tx_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "droppedRx": "dropped_rx", 
        "droppedRxDelta": "dropped_rx_delta", 
        "droppedRxDeltaAvg": "dropped_rx_delta_avg", 
        "droppedRxDeltaMax": "dropped_rx_delta_max", 
        "droppedRxDeltaMin": "dropped_rx_delta_min", 
        "droppedTx": "dropped_tx", 
        "droppedTxDelta": "dropped_tx_delta", 
        "droppedTxDeltaAvg": "dropped_tx_delta_avg", 
        "droppedTxDeltaMax": "dropped_tx_delta_max", 
        "droppedTxDeltaMin": "dropped_tx_delta_min", 
        "errorsRx": "errors_rx", 
        "errorsRxDelta": "errors_rx_delta", 
        "errorsRxDeltaAvg": "errors_rx_delta_avg", 
        "errorsRxDeltaMax": "errors_rx_delta_max", 
        "errorsRxDeltaMin": "errors_rx_delta_min", 
        "errorsTx": "errors_tx", 
        "errorsTxDelta": "errors_tx_delta", 
        "errorsTxDeltaAvg": "errors_tx_delta_avg", 
        "errorsTxDeltaMax": "errors_tx_delta_max", 
        "errorsTxDeltaMin": "errors_tx_delta_min", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "packetsRx": "packets_rx", 
        "packetsRxDelta": "packets_rx_delta", 
        "packetsRxDeltaAvg": "packets_rx_delta_avg", 
        "packetsRxDeltaMax": "packets_rx_delta_max", 
        "packetsRxDeltaMin": "packets_rx_delta_min", 
        "packetsTx": "packets_tx", 
        "packetsTxDelta": "packets_tx_delta", 
        "packetsTxDeltaAvg": "packets_tx_delta_avg", 
        "packetsTxDeltaMax": "packets_tx_delta_max", 
        "packetsTxDeltaMin": "packets_tx_delta_min", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.bytes_rx = None
        self.bytes_rx_delta = None
        self.bytes_rx_delta_avg = None
        self.bytes_rx_delta_max = None
        self.bytes_rx_delta_min = None
        self.bytes_tx = None
        self.bytes_tx_delta = None
        self.bytes_tx_delta_avg = None
        self.bytes_tx_delta_max = None
        self.bytes_tx_delta_min = None
        self.child_action = None
        self.dropped_rx = None
        self.dropped_rx_delta = None
        self.dropped_rx_delta_avg = None
        self.dropped_rx_delta_max = None
        self.dropped_rx_delta_min = None
        self.dropped_tx = None
        self.dropped_tx_delta = None
        self.dropped_tx_delta_avg = None
        self.dropped_tx_delta_max = None
        self.dropped_tx_delta_min = None
        self.errors_rx = None
        self.errors_rx_delta = None
        self.errors_rx_delta_avg = None
        self.errors_rx_delta_max = None
        self.errors_rx_delta_min = None
        self.errors_tx = None
        self.errors_tx_delta = None
        self.errors_tx_delta_avg = None
        self.errors_tx_delta_max = None
        self.errors_tx_delta_min = None
        self.most_recent = None
        self.packets_rx = None
        self.packets_rx_delta = None
        self.packets_rx_delta_avg = None
        self.packets_rx_delta_max = None
        self.packets_rx_delta_min = None
        self.packets_tx = None
        self.packets_tx_delta = None
        self.packets_tx_delta_avg = None
        self.packets_tx_delta_max = None
        self.packets_tx_delta_min = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "EtherFcoeInterfaceStatsHist", parent_mo_or_dn, **kwargs)

