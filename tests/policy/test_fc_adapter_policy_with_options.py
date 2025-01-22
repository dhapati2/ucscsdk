import pytest
from nose import with_setup

from tests.connection.info import get_ethernet_adaptor_params, custom_setup, custom_teardown, get_fc_adaptor_params
from ucscsdk.mometa.adaptor.AdaptorFcCdbWorkQueueProfile import AdaptorFcCdbWorkQueueProfile
from ucscsdk.mometa.adaptor.AdaptorFcErrorRecoveryProfile import AdaptorFcErrorRecoveryProfile
from ucscsdk.mometa.adaptor.AdaptorFcFnicProfile import AdaptorFcFnicProfile
from ucscsdk.mometa.adaptor.AdaptorFcInterruptProfile import AdaptorFcInterruptProfile
from ucscsdk.mometa.adaptor.AdaptorFcPortFLogiProfile import AdaptorFcPortFLogiProfile
from ucscsdk.mometa.adaptor.AdaptorFcPortPLogiProfile import AdaptorFcPortPLogiProfile
from ucscsdk.mometa.adaptor.AdaptorFcPortProfile import AdaptorFcPortProfile
from ucscsdk.mometa.adaptor.AdaptorFcRecvQueueProfile import AdaptorFcRecvQueueProfile
from ucscsdk.mometa.adaptor.AdaptorFcWorkQueueProfile import AdaptorFcWorkQueueProfile
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
    """
        Creates fibre channel adapter policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_or_dn"]
        policy_name = adapter_params["name"]
        descr = adapter_params["descr"]
        work_cbd_count = adapter_params["work_cbd_count"]
        work_cbd_ring_size = adapter_params["work_cbd_ring_size"]
        plogi_retries = adapter_params["plogi_retries"]
        plogi_timeout = adapter_params["plogi_timeout"]
        flogi_retries = adapter_params["flogi_retries"]
        flogi_timeout = adapter_params["flogi_timeout"]
        fcp_error_recovery = adapter_params["fcp_error_recovery"]
        link_down_timeout = adapter_params["link_down_timeout"]
        port_down_io_retry_count = adapter_params["port_down_io_retry_count"]
        port_down_timeout=adapter_params["port_down_timeout"]
        work_ring_size = adapter_params["work_ring_size"]
        recv_ring_size = adapter_params["recv_ring_size"]
        io_throttle_count = adapter_params["io_throttle_count"]
        luns_per_target = adapter_params["luns_per_target"]
        io_retry_timeout = adapter_params["io_retry_timeout"]
        lun_queue_depth = adapter_params["lun_queue_depth"]
        mode = adapter_params["mode"]

        adaptor_host_fc_if_profile_mo = AdaptorHostFcIfProfile(descr=descr
                                                              ,parent_mo_or_dn=parent_mo_dn
                                                              ,name=policy_name
                                                              )

        adaptor_fc_cdb_work_queue_profile = AdaptorFcCdbWorkQueueProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                                        ,count = work_cbd_count
                                                                        ,ring_size = work_cbd_ring_size
                                                                         )

        adaptor_fc_port_plogi_profile = AdaptorFcPortPLogiProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                                 ,retries=plogi_retries
                                                                 ,timeout=plogi_timeout
                                                                 )


        adaptor_fc_port_flogi_profile = AdaptorFcPortFLogiProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                                 ,retries=flogi_retries
                                                                 ,timeout=flogi_timeout
                                                                 )

        adaptor_fc_error_recovery_profile = AdaptorFcErrorRecoveryProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                                         ,fcp_error_recovery=fcp_error_recovery
                                                                         ,link_down_timeout=link_down_timeout
                                                                         ,port_down_io_retry_count=port_down_io_retry_count
                                                                         ,port_down_timeout=port_down_timeout
                                                                         )

        adaptor_fc_work_queue_profile = AdaptorFcWorkQueueProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                                 ,ring_size=work_ring_size
                                                                 )

        adaptor_fc_recv_queue_profile = AdaptorFcRecvQueueProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                                 ,ring_size=recv_ring_size
                                                                 )


        adaptor_fc_port_profile = AdaptorFcPortProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                      ,io_throttle_count=io_throttle_count
                                                      ,luns_per_target=luns_per_target
                                                      )

        adaptor_fc_fnic_profile = AdaptorFcFnicProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                       ,io_retry_timeout=io_retry_timeout
                                                       ,lun_queue_depth=lun_queue_depth
                                                      )

        adaptor_fc_interrupt_profile = AdaptorFcInterruptProfile(parent_mo_or_dn=adaptor_host_fc_if_profile_mo
                                                                 ,mode=mode
                                                                 )

        handle.add_mo(adaptor_host_fc_if_profile_mo)
        handle.commit()
        assert adaptor_host_fc_if_profile_mo is not None, "Failed to create FC Adapter policy"

    except Exception as e:
        pytest.fail(f"Error creating FC Adapter policy: {str(e)}")


@with_setup(setup, teardown)
def test_delete_fc_adapter_policy():
    print('delete_fc_adapter_policy() method execution started...............')

    parent_mo_dn = adapter_params["parent_mo_or_dn"]
    policy_name = adapter_params["name"]

    obj = handle.query_dn(parent_mo_dn + "/fc-profile-" + policy_name)
    handle.remove_mo(obj)
    handle.commit()

