import pytest
from nose import with_setup

from tests.connection.info import get_ethernet_adaptor_params, custom_setup, custom_teardown
from ucscsdk.mometa.adaptor.AdaptorEthArfsProfile import AdaptorEthArfsProfile
from ucscsdk.mometa.adaptor.AdaptorEthCompQueueProfile import AdaptorEthCompQueueProfile
from ucscsdk.mometa.adaptor.AdaptorEthFailoverProfile import AdaptorEthFailoverProfile
from ucscsdk.mometa.adaptor.AdaptorEthGENEVEProfile import AdaptorEthGENEVEProfile
from ucscsdk.mometa.adaptor.AdaptorEthInterruptProfile import AdaptorEthInterruptProfile
from ucscsdk.mometa.adaptor.AdaptorEthInterruptScalingProfile import AdaptorEthInterruptScalingProfile
from ucscsdk.mometa.adaptor.AdaptorEthNVGREProfile import AdaptorEthNVGREProfile
from ucscsdk.mometa.adaptor.AdaptorEthOffloadProfile import AdaptorEthOffloadProfile
from ucscsdk.mometa.adaptor.AdaptorEthRecvQueueProfile import AdaptorEthRecvQueueProfile
from ucscsdk.mometa.adaptor.AdaptorEthRoCEProfile import AdaptorEthRoCEProfile
from ucscsdk.mometa.adaptor.AdaptorEthVxLANProfile import AdaptorEthVxLANProfile
from ucscsdk.mometa.adaptor.AdaptorEthWorkQueueProfile import AdaptorEthWorkQueueProfile
from ucscsdk.mometa.adaptor.AdaptorHostEthIfProfile import AdaptorHostEthIfProfile
from ucscsdk.mometa.adaptor.AdaptorIpV6RssHashProfile import AdaptorIpV6RssHashProfile
from ucscsdk.mometa.adaptor.AdaptorRssProfile import AdaptorRssProfile

adapter_params = get_ethernet_adaptor_params()
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)

@with_setup(setup, teardown)
def test_create_ethernet_adapter_policy():
    """
        Creates ethernet adapter policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_or_dn"]
        policy_name = adapter_params["name"]
        descr = adapter_params["descr"]
        pooled_resources = adapter_params["pooled_resources"]
        large_receive = adapter_params["large_receive"]
        tcp_rx_checksum = adapter_params["tcp_rx_checksum"]
        tcp_segment = adapter_params["tcp_segment"]
        tcp_tx_checksum = adapter_params["tcp_tx_checksum"]
        work_count = adapter_params["work_count"]
        work_ring_size = adapter_params["work_ring_size"]
        comp_count = adapter_params["comp_count"]
        offload = adapter_params["offload"]
        recv_count = adapter_params["recv_count"]
        recv_ring_size = adapter_params["recv_ring_size"]
        accelarated_rfs=adapter_params["accelarated_rfs"]
        admin_state = adapter_params["admin_state"]
        cos = adapter_params["cos"]
        memory_regions = adapter_params["memory_regions"]
        prio = adapter_params["prio"]
        queue_pairs = adapter_params["queue_pairs"]
        resource_groups = adapter_params["resource_groups"]
        v1 = adapter_params["v1"]
        v2 = adapter_params["v2"]
        coalescing_time = adapter_params["coalescing_time"]
        coalescing_type = adapter_params["coalescing_type"]
        interrupt_count = adapter_params["interrupt_count"]
        mode = adapter_params["mode"]
        receive_side_scaling = adapter_params["receive_side_scaling"]

        adaptor_host_eth_if_profile_mo = AdaptorHostEthIfProfile(descr=descr
                                                                 , parent_mo_or_dn=parent_mo_dn
                                                                 , name=policy_name
                                                                 , pooled_resources=pooled_resources
                                                                 )

        adaptor_eth_interrupt_scaling_profile_mo = AdaptorEthInterruptScalingProfile(
            parent_mo_or_dn=adaptor_host_eth_if_profile_mo)

        adaptor_ip_v6_rss_hash_profile_mo = AdaptorIpV6RssHashProfile(
            parent_mo_or_dn=adaptor_host_eth_if_profile_mo)

        adaptor_eth_failover_profile_mo = AdaptorEthFailoverProfile(parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                                    , timeout='5')

        adaptor_eth_offload_profile_mo = AdaptorEthOffloadProfile(parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                                  , large_receive=large_receive
                                                                  , tcp_rx_checksum=tcp_rx_checksum
                                                                  , tcp_segment=tcp_segment
                                                                  , tcp_tx_checksum=tcp_tx_checksum
                                                                  )

        adaptor_eth_work_queue_profile_mo = AdaptorEthWorkQueueProfile(count=work_count,
                                                                       parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                                       , ring_size=work_ring_size
                                                                       )

        adaptor_eth_comp_queue_profile_mo = AdaptorEthCompQueueProfile(count=comp_count,
                                                                       parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                                       )

        adaptor_eth_g_e_n_e_v_e_profile_mo = AdaptorEthGENEVEProfile(parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                                     , offload=offload
                                                                     )

        adaptor_eth_recv_queue_profile_mo = AdaptorEthRecvQueueProfile(count=recv_count,
                                                                       parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                                       , ring_size=recv_ring_size
                                                                       )

        adaptor_eth_vx_l_a_n_profile_mo = AdaptorEthVxLANProfile(parent_mo_or_dn=adaptor_host_eth_if_profile_mo)

        adaptor_eth_n_v_g_r_e_profile_mo = AdaptorEthNVGREProfile(parent_mo_or_dn=adaptor_host_eth_if_profile_mo)

        adaptor_eth_arfs_profile_mo = AdaptorEthArfsProfile(accelarated_rfs=accelarated_rfs
                                                            , parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                            )

        # RDMA over Converged Ethernet (RoCE) - Disabled
        adaptor_eth_ro_c_e_profile_mo = AdaptorEthRoCEProfile(admin_state=admin_state
                                                              , cos=cos
                                                              , parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                              , memory_regions=memory_regions
                                                              , prio=prio
                                                              , queue_pairs=queue_pairs
                                                              , resource_groups=resource_groups
                                                              , v1=v1
                                                              , v2=v2
                                                              )

        adaptor_eth_interrupt_profile_mo = AdaptorEthInterruptProfile(coalescing_time=coalescing_time
                                                                      , coalescing_type=coalescing_type
                                                                      , count=interrupt_count
                                                                      , parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                                      , mode=mode
                                                                      )

        # Receive Side Scaling
        adaptor_rss_profile_mo = AdaptorRssProfile(parent_mo_or_dn=adaptor_host_eth_if_profile_mo
                                                   , receive_side_scaling=receive_side_scaling
                                                   )

        handle.add_mo(adaptor_host_eth_if_profile_mo)
        handle.commit()
        assert adaptor_host_eth_if_profile_mo is not None, "Failed to create Ethernet Adapter policy"

    except Exception as e:
        pytest.fail(f"Error creating Ethernet Adapter policy: {str(e)}")


