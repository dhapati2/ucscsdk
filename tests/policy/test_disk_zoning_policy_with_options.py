import time

import pytest
from nose import with_setup

from tests.connection.info import custom_setup, custom_teardown, get_disk_zoning_params
from ucscsdk.mometa.lstorage.LstorageDiskSlot import LstorageDiskSlot
from ucscsdk.mometa.lstorage.LstorageDiskZoningPolicy import LstorageDiskZoningPolicy

adapter_params = get_disk_zoning_params()
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


@with_setup(setup, teardown)
def test_create_disk_zoning_policy():
    """
        Creates Disk Zoning policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_dn"]
        policy_name = adapter_params["name"]
        descr = adapter_params["descr"]
        preserve_config = adapter_params["preserve_config"]
        id_1 = adapter_params["id_1"]
        id_2 = adapter_params["id_2"]
        id_3 = adapter_params["id_3"]
        id_4 = adapter_params["id_4"]
        id_5 = adapter_params["id_5"]
        id_6 = adapter_params["id_6"]
        id_7 = adapter_params["id_7"]
        id_8 = adapter_params["id_8"]
        id_9 = adapter_params["id_9"]
        id_10 = adapter_params["id_10"]

        mo = LstorageDiskZoningPolicy(parent_mo_or_dn=parent_mo_dn, name=policy_name, descr=descr)

        #mo = LstorageDiskZoningPolicy(parent_mo_or_dn=parent_mo_dn, name=policy_name, descr=descr, preserve_config=preserve_config)

        l_storage_disk_slot_1 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_1)
        l_storage_disk_slot_2 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_2)
        l_storage_disk_slot_3 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_3)
        l_storage_disk_slot_4 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_4)
        l_storage_disk_slot_5 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_5)
        l_storage_disk_slot_6 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_6)
        l_storage_disk_slot_7 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_7)
        l_storage_disk_slot_8 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_8)
        l_storage_disk_slot_9 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_9)
        l_storage_disk_slot_10 = LstorageDiskSlot(parent_mo_or_dn=mo
                                               ,id=id_10)

        handle.add_mo(mo)
        handle.commit()
        assert mo is not None, "Failed to create Disk Zoning policy"

    except Exception as e:
        pytest.fail(f"Error creating Disk Zoning policy: {str(e)}")


@with_setup(setup, teardown)
def test_delete_disk_zoning_policy():
    """
        Delete Disk Zoning policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_or_dn"]
        policy_name = adapter_params["name"]

        obj = handle.query_dn(parent_mo_dn + "/disk-zoning-policy-" + policy_name)
        handle.remove_mo(obj)
        handle.commit()
        assert obj is not None, "Failed to delete Disk Zoning policy"

    except Exception as e:
        pytest.fail(f"Error Deleting Disk Zoning policy: {str(e)}")


