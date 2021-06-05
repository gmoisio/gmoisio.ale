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
module: ale_aos_ping
author: Gilbert MOISIO
version_added: "1.2.0" # of ale_aos collection
short_description: Check SSH connectivity for an ALE OmniSwitch device.
description:
    - Try to connect to an OmniSwitch device. The module check to see is the
      check_string is present in the output returned by find_prompt().
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
    check_string:
        description:
            - String to check in the returned prompt
        required: false
        default: '>'
'''

EXAMPLES = '''
- ale_aos_ping: 
    host: "{{ inventory_hostname }}"
    username: admin
    password: switch
    sshconf: ~/.ssh/config
'''

RETURN = '''
msg:
    description: Message
    returned: On exit and on fail
    type: string
output:
    description: Output returned by find_prompt()
    returned: On fail if check_string is not found
    type: string
Status and completion message that can be displayed with debug var.
'''


def main():

    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type=str, required=True),
            port=dict(type=int, required=False, default=22),
            sshconfig=dict(type=str, required=False, default=None),
            username=dict(type=str, required=True),
            password=dict(type=str, required=True, no_log=True),
            check_string=dict(type=str, required=False, default='>'),
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

    try:
        ssh_conn = ConnectHandler(**net_device)
        output = ssh_conn.find_prompt()
        ssh_conn.disconnect()
        if module.params['check_string'] in output:
            module.exit_json(msg="SSH connection completed successfully")
        else:
            module.fail_json(msg="Failed to detect '%s' in output" %
                             module.params['check_string'],
                             output=output)
    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        module.fail_json(msg="Failed to connect to device (%s)" %
                             (module.params['host']))


if __name__ == '__main__':
    main()
