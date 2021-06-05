******************************
gmoisio.ale_aos.ale_aos_config
******************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module send config commands from a file or a commands list to an ALE OmniSwitch device.

Parameters
----------
.. code-block:: yaml

    host:
        description:
            - Set to {{ inventory_hostname }} or {{ ansible_host }}
        required: true
    port:
        description:
            - SSH connection port
        required: false
        default: 22
    username:
        description:
            - Login username
        required: true
    password:
        description:
            - Login password
        required: true
    file:
        description:
            - Path to the text file with one config command per line
        required: false
        default: ''
    commands:
        description:
            - List of the config commands to run
        required: false
        default: []
    save:
        description:
            - Boolean to save and synchronize memories after changes success
        required: false
        default: false
    backup:
        description:
            - Boolean to backup configuration in a file before changes
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