import pytest
from nose import with_setup

from tests.connection.info import custom_setup, custom_teardown, get_server_qual_params
from ucscsdk.mometa.adaptor.AdaptorCapQual import AdaptorCapQual
from ucscsdk.mometa.compute.ComputePhysicalQual import ComputePhysicalQual
from ucscsdk.mometa.compute.ComputeQual import ComputeQual
from ucscsdk.mometa.memory.MemoryQual import MemoryQual
from ucscsdk.mometa.processor.ProcessorQual import ProcessorQual
from ucscsdk.mometa.storage.StorageQual import StorageQual


adapter_params = get_server_qual_params()
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)

@with_setup(setup, teardown)
def test_create_server_pool_qual_policy():
    """
        Creates Server pool qualification policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_dn"]
        policy_name = adapter_params["name"]
        descr = adapter_params["descr"]
        model = adapter_params["model"]
        diskless = adapter_params["diskless"]
        disk_type  = adapter_params["disk_type"]
        max_cap_memory = adapter_params["max_cap_memory"]
        min_cap_memory  = adapter_params["min_cap_memory"]
        number_of_blocks  = adapter_params["number_of_blocks"]
        number_of_flex_flash_cards  = adapter_params["number_of_flex_flash_cards"]
        per_disk_cap  = adapter_params["per_disk_cap"]
        units  = adapter_params["units"]
        arch  = adapter_params["arch"]
        max_core  = adapter_params["max_core"]
        max_procs  = adapter_params["max_procs"]
        max_threads  = adapter_params["max_threads"]
        min_cores  = adapter_params["min_cores"]
        min_procs  = adapter_params["min_procs"]
        min_threads  = adapter_params["min_threads"]
        model_proc  = adapter_params["model_proc"]
        speed  = adapter_params["speed"]
        stepping  = adapter_params["stepping"]
        adapter_type  = adapter_params["adapter_type"]
        maximum  = adapter_params["maximum"]
        adapter_model  = adapter_params["adapter_model"]
        clock  = adapter_params["clock"]
        latency  = adapter_params["latency"]
        max_cap  = adapter_params["max_cap"]
        min_cap  = adapter_params["min_cap"]
        speed_memory  = adapter_params["speed_memory"]
        units_memory  = adapter_params["units_memory"]
        width  = adapter_params["width"]

        compute_qual = ComputeQual(descr=descr
                                ,parent_mo_or_dn=parent_mo_dn
                                ,name=policy_name
                                )
        compute_physical_qual = ComputePhysicalQual(parent_mo_or_dn=compute_qual
                                                   ,model=model
                                                    )
        memory_qual = MemoryQual(parent_mo_or_dn=compute_qual
                                 ,clock=clock
                                 ,latency=latency
                                 ,max_cap=max_cap_memory
                                 ,min_cap=min_cap_memory
                                 ,speed=speed_memory
                                 ,units=units_memory
                                 ,width=width
                                 )

        processor_qual_mo = ProcessorQual(parent_mo_or_dn=compute_qual
                                          ,arch=arch
                                          ,max_cores=max_core
                                          ,max_procs=max_procs
                                          ,max_threads=max_threads
                                          ,min_cores=min_cores
                                          ,min_procs=min_procs
                                          ,min_threads=min_threads
                                          ,model=model_proc
                                          ,speed=speed
                                          ,stepping=stepping
                                          )
        adapter_cap_qual_mo = AdaptorCapQual(parent_mo_or_dn=parent_mo_dn
                                             ,type=adapter_type
                                             ,maximum=maximum
                                             ,model=adapter_model
                                             )
        storage_qual = StorageQual(parent_mo_or_dn=parent_mo_dn
                                   ,diskless=diskless
                                   ,disk_type=disk_type
                                   ,max_cap=max_cap
                                   ,min_cap=min_cap
                                   ,number_of_blocks=number_of_blocks
                                   ,number_of_flex_flash_cards=number_of_flex_flash_cards
                                   ,per_disk_cap=per_disk_cap
                                   ,units=units
                                   )

        handle.add_mo(compute_qual)
        handle.commit()
        assert compute_qual is not None, "Failed to create Server pool qualification policy"

    except Exception as e:
        pytest.fail(f"Error creating Server pool qualification policy: {str(e)}")

@with_setup(setup, teardown)
def test_delete_server_pool_qual_policy():
    """
        Delete Server pool qualification policy.
    """
    try:
        parent_mo_dn = adapter_params["parent_mo_dn"]
        policy_name = adapter_params["name"]

        obj = handle.query_dn(parent_mo_dn + "/blade-qualifier-" + policy_name)
        handle.remove_mo(obj)
        handle.commit()
        assert obj is not None, "Failed to create Server pool qualification policy"

    except Exception as e:
        pytest.fail(f"Error creating Server pool qualification policy: {str(e)}")


