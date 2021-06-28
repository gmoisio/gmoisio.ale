***************************
gmoisio.ale.ale_aos_command
***************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module sends a list of commands to an ALE OmniSwitch device. A search string can be specified using a I(command) and I(search) dictionary. Program stops as soon as a search string is not found.

Parameters
----------
.. code-block:: yaml

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


Examples
--------
.. code-block:: yaml

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


Authors
~~~~~~~

- Gilbert MOISIO