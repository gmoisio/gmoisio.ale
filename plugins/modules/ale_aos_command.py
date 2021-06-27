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
ANSIBLE_METADATA = {'metadata_version': '1.2',
                    'supported_by': 'community',
                    'status': ['stableinterface']}

DOCUMENTATION = '''
---
module: ale_aos_command
author: Gilbert MOISIO
version_added: "1.2.2" # of ale collection
short_description: Send a command to an ALE OmniSwitch device.
description:
    - Connect to an OmniSwitch device and send a list of commands.
    It can search for a string.
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
    commands:
        description:
            - List of commands to send to the device. A search string can be specified
            using a I(command) and I(search) dictionary. Program stops as soon as a search
            string is not found.
        type: list
        required: true
    timing:
        description:
            - Boolean to run send_command_timing instead of send_command
        type: bool
        required: false
        default: false
'''

EXAMPLES = '''
- gmoisio.ale.ale_aos_command: 
    host: "{{ ansible_host }}"
    username: admin
    password: switch
    sshconfig: ~/.ssh/config
    commands:
      - show running-directory
      - show vlan

- gmoisio.ale.ale_aos_command: 
    host: "{{ ansible_host }}"
    username: admin
    password: switch
    commands:
      - command: show running-directory
        search: "Running Configuration    : SYNCHRONIZED"
      - command: show vlan
'''

RETURN = '''
msg:
    description: Error message
    returned: On fail
    type: str
output:
    description: Output returned by the commands
    returned: On exit and on fail if the search string is not found
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
            commands=dict(type=list, required=True),
            timing=dict(type=bool, required=False, default=False),
        ),
        supports_check_mode=False)

    net_device = {
        'device_type': 'alcatel_aos',
        'ip': module.params['host'],
        'port': module.params['port'],
        'ssh_config_file': module.params['sshconfig'],
        'username': module.params['username'],
        'password': module.params['password'],
    }

    output = {}

    try:
        ssh_conn = ConnectHandler(**net_device)
        send_command_used = ssh_conn.send_command_timing if module.params['timing'] \
            else ssh_conn.send_command
        for one_command in module.params['commands']:
            command = one_command['command'] if 'command' in one_command \
                else one_command
            output[command] = send_command_used(command)
            if 'search' in one_command and one_command['search'] not in output[command]:
                ssh_conn.disconnect()
                module.fail_json(msg="Search string (%s) not in command output" %
                                 (one_command['search']), output=output)
        ssh_conn.disconnect()
        if 'ERROR' in output:
            module.fail_json(msg="Error in command execution", output=output)
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
