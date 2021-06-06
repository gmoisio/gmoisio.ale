*************************
gmoisio.ale.ale_aos_facts
*************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module get ALE OmniSwitch device informations and return a dictionary of lists.

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
    getters:
        description:
            - List of the getters to retrieve
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

Authors
~~~~~~~

- Gilbert MOISIO