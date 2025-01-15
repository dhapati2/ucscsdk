import time

import pytest
from nose import with_setup

from tests.connection.info import custom_setup, custom_teardown, get_disk_zoning_params
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
        mo = LstorageDiskZoningPolicy(parent_mo_or_dn=parent_mo_dn, name=policy_name, descr=descr)
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


