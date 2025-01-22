import time

import pytest
from nose import with_setup

from tests.connection.info import custom_setup, custom_teardown, get_disk_zoning_params
from ucscsdk.mometa.lstorage.LstorageControllerRef import LstorageControllerRef
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
        server_id = adapter_params["server_id"]
        controller_id = adapter_params["controller_id"]
        controller_type = adapter_params["controller_type"]
        unassigned_from = int(adapter_params["unassigned_from"])
        unassigned_to = int(adapter_params["unassigned_to"])
        dedicated_from = int(adapter_params["dedicated_from"])
        dedicated_to = int(adapter_params["dedicated_from"])
        chassis_from = int(adapter_params["chassis_from"])
        chassis_to =int(adapter_params["chassis_from"])
        shared_from = int(adapter_params["shared_from"])
        shared_to = int(adapter_params["shared_to"])

        mo = LstorageDiskZoningPolicy(parent_mo_or_dn=parent_mo_dn, name=policy_name, descr=descr, preserve_config=preserve_config)

        for i in range(unassigned_from, unassigned_to):
            unassigned_mo = LstorageDiskSlot(parent_mo_or_dn=mo, id=str(i))
            unassigned_mo.ownership = 'unassigned'

        for j in range(dedicated_from, dedicated_to):
            dedicated_mo = LstorageDiskSlot(parent_mo_or_dn=mo, id=str(j))
            dedicated_mo.drive_path = 'PATH-BOTH'
            dedicated_mo.ownership = 'dedicated'
            controller_ref = LstorageControllerRef(parent_mo_or_dn=dedicated_mo, server_id=server_id,
                                                   controller_type=controller_type, controller_id=controller_id)

        for k in range(shared_from, shared_to):
            dedicated_mo = LstorageDiskSlot(parent_mo_or_dn=mo, id=str(k))
            dedicated_mo.drive_path = 'PATH-BOTH'
            dedicated_mo.ownership = 'shared'
            controller_ref = LstorageControllerRef(parent_mo_or_dn=dedicated_mo, server_id=server_id,
                                                   controller_type=controller_type, controller_id=controller_id)

        for l in range(chassis_from, chassis_to):
            dedicated_mo = LstorageDiskSlot(parent_mo_or_dn=mo, id=str(l))
            dedicated_mo.drive_path = 'PATH-BOTH'
            dedicated_mo.ownership = 'chassis-global-spare'
            controller_ref = LstorageControllerRef(parent_mo_or_dn=dedicated_mo, server_id=server_id,
                                                   controller_type=controller_type, controller_id=controller_id)

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
        parent_mo_dn = adapter_params["parent_mo_dn"]
        policy_name = adapter_params["name"]

        obj = handle.query_dn(parent_mo_dn + "/disk-zoning-policy-" + policy_name)
        handle.remove_mo(obj)
        handle.commit()
        assert obj is not None, "Failed to delete Disk Zoning policy"

    except Exception as e:
        pytest.fail(f"Error Deleting Disk Zoning policy: {str(e)}")


