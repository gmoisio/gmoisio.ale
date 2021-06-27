#!/usr/bin/env python

# Copyright (c) 2021, Gilbert MOISIO
#
# All rights reserved.
#
# License: CC BY-NC-ND 4.0
#          Attribution-NonCommercial-NoDerivatives 4.0 International
#
# You are free to:
#
# Share — copy and redistribute the material in any medium or format
#
# Under the following terms:
#
# Attribution   — You must give appropriate credit, provide a link to the
#                 license, and indicate if changes were made. You may do so in
#                 any reasonable manner, but not in any way that suggests the
#                 licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# NoDerivatives — If you remix, transform, or build upon the material, you may
#                 not distribute the modified material.
# No additional restrictions — You may not apply legal terms or technological
#                              measures that legally restrict others from doing
#                              anything the license permits.
#

from netmiko.ssh_exception import *
from netmiko import ConnectHandler
from ansible.module_utils.basic import AnsibleModule
from re import findall
ANSIBLE_METADATA = {'metadata_version': '1.2',
                    'supported_by': 'community',
                    'status': ['stableinterface']}

DOCUMENTATION = '''
---
module: ale_aos_facts
author: Gilbert MOISIO
version_added: "1.2.2" # of ale collection
short_description: Get ALE OmniSwitch device informations and return a dictionary of lists.
description:
    - Get device informations using getters selector and return a
      dictionary formatted output.
requirements:
    - netmiko >= 3.4.0
options:
    host:
        description:
            - Set to {{ inventory_hostname }} or {{ ansible_host }}
        type: str
        required: true
    port:
        description:
            - SSH connection port
        type: int
        required: false
        default: 22
    sshconfig:
        description:
            - Path to sshconfig to use for connections
        type: str
        required: false
        default: None
    username:
        description:
            - Login username
        type: str
        required: true
    password:
        description:
            - Login password
        type: str
        required: true
    getters:
        description:
            - List of the getters to retrieve
        type: list
        required: false
        default: [vlans]
'''

EXAMPLES = '''
- gmoisio.ale.ale_aos_facts: 
    host: "{{ ansible_host }}"
    username: admin
    password: switch
    sshconfig: ~/.ssh/config
    getters:
        - vlans
        - interfaces
        - ntp
'''

RETURN = '''
msg:
    description: Message
    returned: On exit and on fail
    type: string
output:
    description: Dictionary of lists returned by the commands
    returned: On exit
    type: dict
'''


def main():

    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type=str, required=True),
            port=dict(type=int, required=False, default=22),
            sshconfig=dict(type=str, required=False, default=None),
            username=dict(type=str, required=True),
            password=dict(type=str, required=True, no_log=True),
            getters=dict(type=list, required=False, default=['vlans']),
        ),
        supports_check_mode=False)

    net_device = {
        'device_type': 'alcatel_aos',
        'ip': module.params['host'],
        'port': module.params['port'],
        'ssh_config_file': module.params['sshconfig'],
        'username': module.params['username'],
        'password': module.params['password'],
        'timeout': 10,
    }

    getters_list = {
        'vlans': [
            'show vlan',
            '(?P<vlan_id>\d{1,4})(?:.*)'
        ],
        'interfaces': [
            'show interfaces status',
            '(?P<interface>\d\S+)(?:.*)'
        ],
        'ntp': [
            'show ntp server status',
            '(?:Host name\s+=\s)(?P<ntp_server>\w\S+)(?:,)'
        ],
    }

    output = {}
    bad_getters = []

    try:
        ssh_conn = ConnectHandler(**net_device)
        for getter in module.params['getters']:
            if getter in list(getters_list.keys()):
                result = ssh_conn.send_command(
                    getters_list[getter][0])
                output[getter] = findall(getters_list[getter][1], result)
            else:
                bad_getters.append(getter)
        ssh_conn.disconnect()
        if bad_getters:
            module.fail_json(msg="Please check getters, (%s) not available" %
                             str(bad_getters).strip('[]'))
        else:
            module.exit_json(output=output)
    except (NetMikoAuthenticationException):
        module.fail_json(msg="Failed to authenticate to device (%s)" %
                             (module.params['host']))
    except (NetMikoTimeoutException):
        module.fail_json(msg="Timeout when trying to connect to device (%s)" %
                             (module.params['host']))
    except (ConfigInvalidException):
        module.fail_json(msg="Invalid configuration for device (%s)" %
                             (module.params['host']))


if __name__ == '__main__':
    main()
