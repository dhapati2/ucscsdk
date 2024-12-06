from nose.tools import with_setup

from ..connection.info import custom_setup, custom_teardown, get_policy_params

handle = None
hfp_policy_params = get_policy_params('hfp')

def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


@with_setup(setup, teardown)
def test_001_create_hfp_policy():

    """Test case creating Host Firmware Package policy"""

    from ucscsdk.mometa.firmware.FirmwareComputeHostPack import\
        FirmwareComputeHostPack

    policy_name = hfp_policy_params['hfp_policy_name']
    parent_mo_dn = hfp_policy_params['hfp_parent_dn']


    mo = FirmwareComputeHostPack(parent_mo_or_dn=parent_mo_dn,
                            name=policy_name,
                            descr="Custom hfp policy description",
                            rack_bundle_version="4.3(4c)C",
                            blade_bundle_version='4.2(3e)B')

    handle.add_mo(mo, True)
    handle.commit()

    mo = handle.query_dn(parent_mo_dn+"/fw-host-pack-"+policy_name)

     # Assert: Checking Host Firmware Package policy created or not.
    assert mo is not None, f"Host Firmware Package policy with name {policy_name} should have been created."


@with_setup(setup, teardown)
def test_002_exclude_server_components():

    """Test case exclude server components from include component list"""

    from ucscsdk.mometa.firmware.FirmwareExcludeServerComponent import\
        FirmwareExcludeServerComponent

    policy_name = hfp_policy_params['hfp_policy_name']
    parent_mo_dn = hfp_policy_params['hfp_parent_dn']
    server_component = hfp_policy_params['hfp_server_component']

    mo = handle.query_dn(parent_mo_dn + "/fw-host-pack-" + policy_name)

    mo_1 = FirmwareExcludeServerComponent(parent_mo_or_dn=mo,
                            server_component=server_component)


    handle.add_mo(mo_1, True)
    handle.commit()

    mo = handle.query_dn(parent_mo_dn+"/exclude-server-component-"+server_component)

     # Assert: Checking Host Firmware Package policy server components excluded or not.
    assert mo_1 is not None, f"Host Firmware Package policy components with {server_component} should have been excluded."


@with_setup(setup, teardown)
def test_003_include_server_components():

    """Test case include server components to include component list"""

    policy_name = hfp_policy_params['hfp_policy_name']
    parent_mo_dn = hfp_policy_params['hfp_parent_dn']
    server_component = hfp_policy_params['hfp_server_component']

    obj = handle.query_dn(parent_mo_dn+"/fw-host-pack-"+policy_name+"/exclude-server-component-"+server_component)

    handle.remove_mo(obj)
    handle.commit()

    mo = handle.query_dn(parent_mo_dn+"/fw-host-pack-"+policy_name+"/exclude-server-component-"+server_component)

    # Assert: Checking server component included or not.
    assert mo is None, f"Host Firmware Package policy server compoents with name {server_component} should have been included"


@with_setup(setup, teardown)
def test_004_remove_hfp_policy():

    """Test case deleting Host Firmware Package policy"""

    policy_name = hfp_policy_params['hfp_policy_name']
    parent_mo_dn = hfp_policy_params['hfp_parent_dn']

    obj = handle.query_dn(parent_mo_dn+"/fw-host-pack-"+policy_name)

    handle.remove_mo(obj)
    handle.commit()

    mo = handle.query_dn(parent_mo_dn+"/fw-host-pack-"+policy_name)

    # Assert: Checking Host Firmware Package policy deleted or not.
    assert mo is None, f"Host Firmware Package policy with name {policy_name} should have been deleted"

