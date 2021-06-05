*******************************
gmoisio.ale_aos.ale_aos_command
*******************************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This module send a command to an ALE OmniSwitch device.

Parameters
----------
.. code-block:: yaml

    host:
        description:
            - Set to {{ inventory_hostname }}
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
            - Boolean to run send_command_timing instead of send_command, useful
              to avoid the limitation on AOS6 when trying to get the configuration
        required: false
        default: false


Examples
--------
.. code-block:: yaml

    - ale_aos_command: 
      host: "{{ inventory_hostname }}"
      username: admin
      password: switch
      command: show running-directory
      search: "Running Configuration    : SYNCHRONIZED"


Authors
~~~~~~~

- Gilbert MOISIO