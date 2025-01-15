import time

import pytest
from nose import with_setup

from tests.connection.info import custom_setup, custom_teardown, get_ethernet_adaptor_params
from ucscsdk.mometa.adaptor.AdaptorHostEthIfProfile import AdaptorHostEthIfProfile

adapter_params = get_ethernet_adaptor_params()
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)

@pytest.mark.first
@with_setup(setup, teardown)
def test_create_ethernet_adapter_policy():
    """
        Creates ethernet adapter policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_or_dn"]
        policy_name = adapter_params["name"]
        descr = adapter_params["descr"]
        mo = AdaptorHostEthIfProfile(parent_mo_or_dn=parent_mo_dn, name=policy_name, descr=descr)
        handle.add_mo(mo)
        handle.commit()
        assert mo is not None, "Failed to create Ethernet Adapter policy"

    except Exception as e:
        pytest.fail(f"Error creating Ethernet Adapter policy: {str(e)}")


@pytest.mark.order(2)
@with_setup(setup, teardown)
def test_update_ethernet_adapter_policy():
    """
        Update ethernet adapter policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_or_dn"]
        policy_name = adapter_params["name"]
        obj = handle.query_dn(parent_mo_dn + "/eth-profile-" + policy_name)
        obj.descr = "updatedEthernetAdapterPolicy"
        handle.set_mo(obj)
        handle.commit()
        assert obj is not None, "Failed to create Ethernet Adapter policy"

    except Exception as e:
        pytest.fail(f"Error creating Ethernet Adapter policy: {str(e)}")


@pytest.mark.order(3)
@with_setup(setup, teardown)
def test_delete_ethernet_adapter_policy():
    """
        Delete ethernet adapter policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_or_dn"]
        policy_name = adapter_params["name"]

        obj = handle.query_dn(parent_mo_dn + "/eth-profile-" + policy_name)
        handle.remove_mo(obj)
        handle.commit()
        assert obj is not None, "Failed to create Ethernet Adapter policy"

    except Exception as e:
        pytest.fail(f"Error creating Ethernet Adapter policy: {str(e)}")


