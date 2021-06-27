*************************
gmoisio.ale.ale_aos_facts
*************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module gets ALE OmniSwitch device informations and return a dictionary of lists.

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
    getters:
        description:
            - List of the getters to retrieve
        type: list
        required: false
        default: [vlans]

Examples
--------
.. code-block:: yaml

    - gmoisio.ale.ale_aos_facts: 
        host: "{{ ansible_host }}"
        username: admin
        password: switch
        getters:
            - vlans
            - interfaces
            - ntp

The module returns a dictionary of lists. It's an experimental module to loop on Python formated informations.

Authors
~~~~~~~

- Gilbert MOISIO