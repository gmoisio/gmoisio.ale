**************************
gmoisio.ale.ale_aos_config
**************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module sends config commands from a file or a commands list to an ALE OmniSwitch device.

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
    file:
        description:
            - Path to the text file with one config command per line
        type: str
        required: false
        default: ''
    commands:
        description:
            - List of the config commands to run
        type: list
        required: false
        default: []
    save:
        description:
            - Boolean to save and synchronize memories after changes success
        type: bool
        required: false
        default: false
    backup:
        description:
            - Boolean to backup configuration in backups/file before changes
        type: bool
        required: false
        default: false


Examples
--------
.. code-block:: yaml

    - gmoisio.ale.ale_aos_config: 
        host: "{{ ansible_host }}"
        username: admin
        password: switch
        commands:
        - vlan 100 enable name test1
        - vlan 200 enable name test2

    - gmoisio.ale.ale_aos_config: 
        host: "{{ ansible_host }}"
        username: admin
        password: switch
        file: commands.txt

    Tip to display differences: ansible-playbook myplaybook.yml --diff -v


Authors
~~~~~~~

- Gilbert MOISIO