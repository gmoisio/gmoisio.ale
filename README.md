# Ansible Collection - gmoisio.ale_aos

[![Build Status](https://travis-ci.org/gmoisio/ansible-aos-stdlib.svg?branch=master)](https://travis-ci.org/gmoisio/ansible-aos-stdlib)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-ale_aos-blue.svg)](https://galaxy.ansible.com/gmoisio/ale_aos)

ALE_AOS
=======

An Ansible collection to access Alcatel-Lucent Enterprise OmniSwitch devices.

Requirements
------------

Requires ansible-base >= 2.10.10 and netmiko >= 3.4.0

Example Playbook
----------------

~~~~
- name: This is a test for ale_aos_ping module
  hosts: ale
  connection: local
  roles:
    - gmoisio.ale_aos
  vars:
    ansible_python_interpreter: "python"
  tasks:
    - name: Test ale_aos_ping Python module
      ale_aos_ping: 
        host: "{{ inventory_hostname }}"
        username: admin
        password: switch
      register: result
    - debug: var=result 
~~~~

Add below setting to your ansible.cfg and get a better display:

~~~~
[defaults]
stdout_callback = yaml
~~~~

License
-------

Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).

Author Information
------------------

Gilbert MOISIO, Network & Methodology Senior Consultant.
