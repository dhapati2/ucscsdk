# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from nose.plugins.skip import SkipTest
try:
    import ConfigParser
except:
    import configparser as ConfigParser


def custom_setup():
    from ucscsdk.ucschandle import UcscHandle
    host = "ucscentral"

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))

    hostname = config.get(host, "hostname")
    username = config.get(host, "username")
    password = config.get(host, "password")
    try:
        port = config.get(host, "port")
    except:
        port = 443
    handle = UcscHandle(hostname, username, password, port=port)
    handle.login()
    return handle


def custom_teardown(handle):
    handle.logout()


def get_local_config_params(section):

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    local = {}
    try:
        local['file_dir'] = config.get(section, "file_dir")
        local['file_name'] = config.get(section, "file_name")
        for value in local.values():
            if not value or value.isspace():
                raise
    except:
        local = None
    return local


def get_remote_config_params(section):

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    remote = {}
    try:
        remote['hostname'] = config.get(section, "hostname")
        remote['username'] = config.get(section, "username")
        remote['password'] = config.get(section, "password")
        remote['protocol'] = config.get(section, "protocol")
        remote['file_dir'] = config.get(section, "file_dir")
        remote['file_name'] = config.get(section, "file_name")
        for value in remote.values():
            if not value or value.isspace():
                raise
    except:
        remote = None
    return remote


def get_domain_params(number_of_domains=1):
    section = "domain"

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    domains = []
    try:
        for x in range(number_of_domains):
            domain = {}
            domain['ip'] = config.get(section, "domain_ip_%s" % x)
            domain['username'] = config.get(section, "domain_username_%s" % x)
            domain['password'] = config.get(section, "domain_password_%s" % x)
            domain['group'] = config.get(section, "domain_group_%s" % x)
            domain['id'] = config.get(section, "domain_id_%s" % x)

            for value in domain.values():
                if not value or value.isspace():
                    raise
            domains.append(domain)
    except:
        domains = None
    return domains


def get_cisco_account_params():
    section = "cisco_account"

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    cisco_account = {}
    try:
        cisco_account['username'] = config.get(section, "username")
        cisco_account['password'] = config.get(section, "password")
        cisco_account['proxy_host'] = config.get(section, "proxy_host")
        cisco_account['proxy_port'] = config.get(section, "proxy_port")
        cisco_account['proxy_username'] = config.get(section, "proxy_username")
        cisco_account['proxy_password'] = config.get(section, "proxy_password")
        for value in cisco_account.values():
            if not value or value.isspace():
                raise
    except:
        cisco_account = None
    return cisco_account


def skipped(reason=None):
    def wrap(func):
        def f():
            raise SkipTest("Test %s is skipped, reason: '%s'"
                           % (func.__name__,
                              "Not specified" if reason is None else reason))
        f.__name__ = func.__name__
        return f
    return wrap

def get_policy_params(policy_name):
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    section = 'policy'
    policy = {}
    try:
        policy[policy_name+'_policy_name'] = config.get(section, policy_name+"_policy_name")
        policy[policy_name+'_parent_dn'] = config.get(section, policy_name+"_parent_dn")

        if (policy_name is not 'compute_connection' and policy_name is not 'bios' and policy_name is not 'power_sync'
            and policy_name is not 'scrub' and policy_name is not 'vmedia'and policy_name is not 'ipmi' and
            policy_name is not 'power_control' and policy_name is not 'hfp' and policy_name is not 'graphics_card'):
            policy[policy_name + '_mode'] = config.get(section, policy_name + "_mode")

        if policy_name is 'boot':
            policy[policy_name + '_reboot_on_update'] = config.get(section, policy_name + "_reboot_on_update")
            policy[policy_name + '_enforce_vnic_name'] = config.get(section, policy_name + "_enforce_vnic_name")

        if policy_name is 'scrub':
            policy[policy_name + '_flex_flash_scrub'] = config.get(section, policy_name + "_flex_flash_scrub")
            policy[policy_name + '_bios_settings_scrub'] = config.get(section, policy_name + "_bios_settings_scrub")
            policy[policy_name + '_disk_scrub'] = config.get(section, policy_name + "_disk_scrub")

        if policy_name is 'vmedia':
            policy[policy_name + '_retry_on_mount_fail'] = config.get(section, policy_name + "_retry_on_mount_fail")
            policy[policy_name + '_hdd_mapping_name'] = config.get(section, policy_name + "_hdd_mapping_name")
            policy[policy_name + '_cdd_mapping_name'] = config.get(section, policy_name + "_cdd_mapping_name")
            policy[policy_name + '_hdd_device_type'] = config.get(section, policy_name + "_hdd_device_type")
            policy[policy_name + '_cdd_device_type'] = config.get(section, policy_name + "_cdd_device_type")
            policy[policy_name + '_mount_protocol'] = config.get(section, policy_name + "_mount_protocol")
            policy[policy_name + '_remote_ip_address'] = config.get(section, policy_name + "_remote_ip_address")
            policy[policy_name + '_image_file_name'] = config.get(section, policy_name + "_image_file_name")
            policy[policy_name + '_image_path'] = config.get(section, policy_name + "_image_path")
            policy[policy_name + '_user_id'] = config.get(section, policy_name + "_user_id")
            policy[policy_name + '_password'] = config.get(section, policy_name + "_password")

        if policy_name is 'ipmi':
            policy[policy_name + '_user_name'] = config.get(section, policy_name + "_user_name")
            policy[policy_name + '_pwd'] = config.get(section, policy_name + "_pwd")
            policy[policy_name + '_sol_access'] = config.get(section, policy_name + "_sol_access")
            policy[policy_name + '_over_lan'] = config.get(section, policy_name + "_over_lan")

        if policy_name is 'power_control':
            policy[policy_name + '_fan_speed'] = config.get(section, policy_name + "_fan_speed")
            policy[policy_name + '_prio'] = config.get(section, policy_name + "_prio")

        if policy_name is 'hfp':
            policy[policy_name + '_server_component'] = config.get(section, policy_name + "_server_component")

        if policy_name is 'graphics_card':
            policy[policy_name + '_mode'] = config.get(section, policy_name + "_mode")

        else:
            if policy_name is 'localdiskconfig':
                policy[policy_name + '_protect_config'] = config.get(section, policy_name + "_protect_config")
                policy[policy_name + '_reporting_state'] = config.get(section, policy_name + "_reporting_state")
                policy[policy_name + '_flex_flash_state'] = config.get(section, policy_name + "_flex_flash_state")
            else:
                if policy_name is 'compute_connection':
                    policy[policy_name + '_server_sioc_connectivity'] = config.get(section, policy_name + "_server_sioc_connectivity")

        for value in policy.values():
            if not value or value.isspace():
                raise
    except:
        policy = None

    return policy

def get_pool_params(pool_name):
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    section = 'pool'
    pool = {}
    try:
        pool[pool_name+'_pool_name'] = config.get(section, pool_name+"_pool_name")
        pool[pool_name+'_parent_dn'] = config.get(section, pool_name+"_parent_dn")
        pool[pool_name + '_r_from'] = config.get(section, pool_name + "_r_from")
        pool[pool_name + '_to'] = config.get(section, pool_name + "_to")

        if pool_name is 'ip':
            pool[pool_name + '_prefix'] = config.get(section, pool_name + "_prefix")
            pool[pool_name + '_def_gw'] = config.get(section, pool_name + "_def_gw")
            pool[pool_name+'_prim_dns'] = config.get(section, pool_name+"_prim_dns")
            pool[pool_name+'_sec_dns'] = config.get(section, pool_name+"_sec_dns")
            pool[pool_name+'_subnet'] = config.get(section, pool_name+"_subnet")

        if pool_name is 'iqn':
            pool[pool_name + '_prefix'] = config.get(section, pool_name + "_prefix")
            pool[pool_name + '_suffix'] = config.get(section, pool_name + "_suffix")

        for value in pool.values():
            if not value or value.isspace():
                raise
    except:
        pool = None

    return pool

def get_schedule_params(schedule_name):
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    section = 'schedule'
    schedule = {}
    try:
        schedule['schedule_name'] = config.get(section,"schedule_name")
        schedule['domain_group'] = config.get(section, "domain_group")
        schedule['parent_mo_or_dn'] = config.get(section, "parent_mo_or_dn")
        schedule['one_time_sch_name'] = config.get(section,  "one_time_sch_name")
        schedule['recurring_sch_name'] = config.get(section,  "recurring_sch_name")
        schedule['sch_date'] = config.get(section, "sch_date")
        schedule['proc_cap'] = config.get(section, "proc_cap")
        schedule['proc_break'] = config.get(section, "proc_break")
        schedule['time_cap'] = config.get(section, "time_cap")
        schedule['concur_cap'] = config.get(section, "concur_cap")
        schedule['start_date'] = config.get(section,  "start_date")
        schedule['day'] = config.get(section, "day")

        for value in schedule.values():
            if not value or value.isspace():
                raise
    except:
        schedule = None

    return schedule

