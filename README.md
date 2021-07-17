# Ansible Collection - gmoisio.ale

[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gmoisio.ale-blue.svg)](https://galaxy.ansible.com/gmoisio/gmoisio.ale)

# ALE

An Ansible collection to access Alcatel-Lucent Enterprise OmniSwitch devices.

## Modules

| Name                                                                                                                 | Description                                                                            |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [gmoisio.ale.ale_aos_ping](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale.ale_aos_ping.rst)       | Check SSH connectivity for an ALE OmniSwitch device                                    |
| [gmoisio.ale.ale_aos_command](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale.ale_aos_command.rst) | Send a list of commands to an ALE OmniSwitch device                                    |
| [gmoisio.ale.ale_aos_config](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale.ale_aos_config.rst)   | Send config commands to an ALE OmniSwitch device                                       |
| [gmoisio.ale.ale_aos_facts](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale.ale_aos_facts.rst)     | Get ALE OmniSwitch device informations and return a dictionary of lists (experimental) |

## Filters

| Name                                                                                                   | Description                   |
| ------------------------------------------------------------------------------------------------------ | ----------------------------- |
| [gmoisio.ale.validate](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale.validate.rst) | Validate vars against schemas |

## Release notes

<details open>
  <summary>v1.3.0</summary>

> Released on July 17, 2021

[gmoisio.ale.validate](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale.validate.rst) filter requires Cerberus to validate vars against YAML schemas

~~~~shell
pip install cerberus
~~~~

~~~~jinja
{% for vlan in vlans | gmoisio.ale.validate(vlans_schema) %}
vlan {{ vlan.id }} admin-state enable name {{ vlan.name }}
{% endfor %}
~~~~

~~~~yaml
- name: Validate Source of Truth
  ansible.builtin.assert:
    that :
      - hostvars[inventory_hostname]['vlans'] | gmoisio.ale.validate(vlans_schema, True)
      - hostvars[inventory_hostname]['ntp_servers'] | gmoisio.ale.validate(ntp_servers_schema, True)
~~~~
</details>

<details>
  <summary>v1.2.2</summary>

> Released on June 26, 2021

[gmoisio.ale.ale_aos_command](https://github.com/gmoisio/gmoisio.ale/blob/main/docs/gmoisio.ale.ale_aos_command.rst) needs a list as input

~~~~yaml
---
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
~~~~
</details>

## Requirements

Requires ansible-base >= 2.10.10, netmiko >= 3.4.0 and cerberus >= 1.3.4

## Example Playbook

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

## Dealing with password

Password can be defined as a single encrypted variable in a YAML file.

~~~~yaml
password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          ....
~~~~

To decrypt it at run time, there are two options:
- Use the `--ask-vault-pass` option on the command line.
- Use a file with the vault decryption password and configure the `vault_password_file` in `ansible.cfg`.

## Dealing with old AOS6 release

When there is an issue with SSH connection (SSH crypto algorithm issue), the workaround is to use the `sshconf` module option.

~~~~
sshconf: ~/.ssh/config
~~~~

With the config file `~/.ssh/config`

~~~~
Host xx.yy.zz.ww
    HostKeyAlgorithms +ssh-dss
~~~~

## Improved display

YAML format can improve playbooks display with `stdout_callback = yaml` in `ansible.cfg` file.
It needs the `community.general` Ansible collection to work fine.

## License

Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).

## Author Information

Gilbert MOISIO, Network & Methodology Senior Consultant.