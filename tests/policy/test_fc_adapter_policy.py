
from nose import with_setup

from tests.connection.info import custom_setup, custom_teardown, get_fc_adaptor_params
from ucscsdk.mometa.adaptor.AdaptorHostFcIfProfile import AdaptorHostFcIfProfile

adapter_params = get_fc_adaptor_params()
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


@with_setup(setup, teardown)
def test_create_fc_adapter_policy():
    print('create_fc_adapter_policy() method execution started...............')

    parent_mo_dn=adapter_params["parent_mo_or_dn"]
    policy_name=adapter_params["name"]
    descr=adapter_params["descr"]

    mo = AdaptorHostFcIfProfile(parent_mo_or_dn=parent_mo_dn,name=policy_name,descr=descr)
    handle.add_mo(mo)
    handle.commit()


@with_setup(setup, teardown)
def test_delete_fc_adapter_policy():
    print('delete_fc_adapter_policy() method execution started...............')

    parent_mo_dn = adapter_params["parent_mo_or_dn"]
    policy_name = adapter_params["name"]

    obj = handle.query_dn(parent_mo_dn + "/fc-profile-" + policy_name)
    handle.remove_mo(obj)
    handle.commit()


@with_setup(setup, teardown)
def test_update_fc_adapter_policy():
    print('update_fc_adapter_policy() method execution started...............')

    parent_mo_dn = adapter_params["parent_mo_or_dn"]
    policy_name = adapter_params["name"]

    obj = handle.query_dn(parent_mo_dn + "/fc-profile-" + policy_name)
    obj.descr = "updated_fc_adapter_policy"
    handle.set_mo(obj)
    handle.commit()


