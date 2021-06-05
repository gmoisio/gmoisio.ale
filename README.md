# Ansible Collection - gmoisio.ale

[![Build Status](https://travis-ci.org/gmoisio/ansible-aos-stdlib.svg?branch=master)](https://travis-ci.org/gmoisio/gmoisio.ale)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gmoisio.ale-blue.svg)](https://galaxy.ansible.com/gmoisio/gmoisio.ale)

ALE
===

An Ansible collection to access Alcatel-Lucent Enterprise OmniSwitch devices.

Requirements
------------

Requires ansible-base >= 2.10.10 and netmiko >= 3.4.0

Example Playbook
----------------

~~~~
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

~~~~
password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          ....
~~~~

To decrypt it at run time, here are two options:
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

License
-------

Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).

Author Information
------------------

Gilbert MOISIO, Network & Methodology Senior Consultant.
