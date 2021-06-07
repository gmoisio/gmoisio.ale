************************
gmoisio.ale.ale_aos_ping
************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module check SSH connectivity for an ALE OmniSwitch device.

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
    check_string:
        description:
            - String to check in the returned prompt
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