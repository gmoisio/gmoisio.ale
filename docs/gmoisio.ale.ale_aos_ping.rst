************************
gmoisio.ale.ale_aos_ping
************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module checks SSH connectivity for an ALE OmniSwitch device.

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
    check_string:
        description:
            - String to check in the returned prompt
        type: str
        required: false
        default: '>'


Examples
--------
.. code-block:: yaml

    - gmoisio.ale.ale_aos_ping: 
        host: "{{ ansible_host }}"
        username: admin
        password: switch


Authors
~~~~~~~

- Gilbert MOISIO