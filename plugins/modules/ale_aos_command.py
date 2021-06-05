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
from ansible.module_utils.basic import *
ANSIBLE_METADATA = {'metadata_version': '1.2',
                    'supported_by': 'community',
                    'status': ['stableinterface']}

DOCUMENTATION = '''
---
module: ale_aos_command
author: Gilbert MOISIO
version_added: "1.2.0" # of ale_aos collection
short_description: Send a command to an ALE OmniSwitch device.
description:
    - Connect to an OmniSwitch device and send a command. It can search for a
      string.
requirements:
    - netmiko >= 3.4.0
options:
    host:
        description:
            - Set to {{ inventory_hostname }}
        required: true
    port:
        description:
            - SSH connection port
        required: false
        default: 22
    sshconf:
        description:
            - Path to sshconfig to use for connections
        required: false
        default: None
    username:
        description:
            - Login username
        required: true
    password:
        description:
            - Login password
        required: true
    command:
        description:
            - Command to send to the device
        required: true
    search:
        description:
            - String to search in the output of the command
              to validate the proper execution
        required: false
        default: ''
    timing:
        description:
            - Boolean to run send_command_timing instead of send_command
        required: false
        default: false
'''

EXAMPLES = '''
- ale_aos_command: 
    host: "{{ inventory_hostname }}"
    username: admin
    password: switch
    sshconf: ~/.ssh/config
    command: show running-directory
    search: "Running Configuration    : SYNCHRONIZED"
'''

RETURN = '''
msg:
    description: Error message
    returned: On fail
    type: string
output:
    description: Output returned by the command
    returned: On exit and on fail if the search string is not found
    type: string
'''


def main():

    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type=str, required=True),
            port=dict(type=int, required=False, default=22),
            sshconfig=dict(type=str, required=False, default=None),
            username=dict(type=str, required=True),
            password=dict(type=str, required=True, no_log=True),
            command=dict(type=str, required=True),
            search=dict(type=str, required=False, default=None),
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

    try:
        ssh_conn = ConnectHandler(**net_device)
        if module.params['timing']:
            output = ssh_conn.send_command_timing(module.params['command'])
        else:
            output = ssh_conn.send_command(module.params['command'])
        ssh_conn.disconnect()
        if 'ERROR' in output:
            module.fail_json(msg="Error in command execution", output=output)
        if module.params['search'] and module.params['search'] not in output:
            module.fail_json(msg="Search string (%s) not in command output" %
                                 (module.params['search']), output=output)
        module.exit_json(output=output)
    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        module.fail_json(msg="Failed to connect to device (%s)" %
                             (module.params['host']))


if __name__ == '__main__':
    main()
