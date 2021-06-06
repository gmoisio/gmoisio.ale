# Ansible Collection - gmoisio.ale

[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gmoisio.ale-blue.svg)](https://galaxy.ansible.com/gmoisio/gmoisio.ale)

ALE
===

An Ansible collection to access Alcatel-Lucent Enterprise OmniSwitch devices.

Modules
-------

| Name                                                                                                                     | Description                                                                            |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| [gmoisio.ale.ale_aos_ping](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale_aos.ale_aos_ping.rst)       | Check SSH connectivity for an ALE OmniSwitch device                                    |
| [gmoisio.ale.ale_aos_command](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale_aos.ale_aos_command.rst) | Send a command to an ALE OmniSwitch device                                             |
| [gmoisio.ale.ale_aos_config](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale_aos.ale_aos_config.rst)   | Send config commands to an ALE OmniSwitch device                                       |
| [gmoisio.ale.ale_aos_facts](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale_aos.ale_aos_facts.rst)     | Get ALE OmniSwitch device informations and return a dictionary of lists (experimental) |

Requirements
------------

Requires ansible-base >= 2.10.10 and netmiko >= 3.4.0

Example Playbook
----------------

~~~~yaml
---
- name: This is a test for ale_aos_ping module
  hosts: ale
  connection: local
  gather_facts: no
  tasks:
    - name: Test ale_aos_ping Python module
      gmoisio.ale.ale_aos_ping: 
        host: "{{ ansible_host }}"
        username: "{{ login }}"
        password: "{{ password }}"
      register: result
    - ansible.builtin.debug: var=result
~~~~

Dealing with password
---------------------

Password can be defined as a single encrypted variable in a YAML file.

~~~~yaml
password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          ....
~~~~

To decrypt it at run time, there are two options:
- Use the `--ask-vault-pass` option on the command line.
- Use a file with the vault decryption password and configure the `vault_password_file` in `ansible.cfg`.

Dealing with old AOS6 release
-----------------------------

When there is an issue with SSH connection (SSH crypto algorithm issue), the workaround is to use the `sshconf` module option.

~~~~
sshconf: ~/.ssh/config
~~~~

With the config file `~/.ssh/config`

~~~~
Host xx.yy.zz.ww
    HostKeyAlgorithms +ssh-dss
~~~~

Improved display
----------------

YAML format can improve playbooks display with `stdout_callback = yaml` in `ansible.cfg` file.
It needs the `community.general` Ansible collection to work fine.

License
-------

Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).

Author Information
------------------

Gilbert MOISIO, Network & Methodology Senior Consultant.