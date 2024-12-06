from nose.tools import with_setup

from ..connection.info import custom_setup, custom_teardown, get_policy_params

handle = None
graphics_card_policy_params = get_policy_params('graphics_card')

def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


@with_setup(setup, teardown)
def test_001_create_graphics_card_policy():

    """Test case creating Graphics card policy"""

    from ucscsdk.mometa.compute.ComputeGraphicsCardPolicy import ComputeGraphicsCardPolicy

    policy_name = graphics_card_policy_params['graphics_card_policy_name']
    parent_mo_dn = graphics_card_policy_params['graphics_card_parent_dn']
    mode = graphics_card_policy_params['graphics_card_mode']

    mo = ComputeGraphicsCardPolicy(parent_mo_or_dn=parent_mo_dn,
                                   name=policy_name,
                                   descr='Custom Graphics card policy description',
                                   graphics_card_mode=mode)

    handle.add_mo(mo, True)
    handle.commit()

    mo = handle.query_dn(parent_mo_dn+"/graphics-card-policy-"+policy_name)

     # Assert: Checking Graphics card policy created or not.
    assert mo is not None, f"Graphics card policy with name {policy_name} should have been created."


@with_setup(setup, teardown)
def test_002_remove_graphics_card_policy():

    """Test case deleting Graphics card policy"""

    policy_name = graphics_card_policy_params['graphics_card_policy_name']
    parent_mo_dn = graphics_card_policy_params['graphics_card_parent_dn']

    obj = handle.query_dn(parent_mo_dn+"/graphics-card-policy-"+policy_name)

    handle.remove_mo(obj)
    handle.commit()

    mo = handle.query_dn(parent_mo_dn+"/graphics-card-policy-"+policy_name)

    # Assert: Checking Graphics card policy deleted or not.
    assert mo is None, f"Graphics card policy with name {policy_name} should have been deleted"

