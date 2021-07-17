********************
gmoisio.ale.validate
********************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This filter allows to validate vars against YAML schemas.
- Jinja2 template stops with error(s) when the vars do not conform to the schema.

Parameters
----------
.. code-block:: yaml

    arguments:
        vars:
            description:
                - Vars to validate that are transmit through the pipe
            type: list
            required: true
        data_schema:
            description:
                - Schema to use for vars validation
            type: list
            required: true
        check:
            description:
                - Boolean that is used to return the vars used for validation or boolean
            type: bool
            required: false
            default: False

    Returns:

      - vars if they validate against schema and check value is False
      - error message if vars do not validate against schema and check value is False
      - boolean True if vars validate against schema and check value is True
      - boolean False if vars do not validate against schema and check value is True

Validation Rules
----------------
Use Cerberus validation rules (see https://docs.python-cerberus.org/en/stable/validation-rules.html)

- allow_unknown
- allowed
- allof
- anyof
- check_with
- contains
- dependencies
- empty
- excludes
- forbidden
- items
- keysrules
- meta
- min, max
- minlength, maxlength
- noneof
- nullable
- *of-rules
- *of-rules typesaver
- oneof
- readonly
- regex
- require_all
- required
- schema (dict)
- schema (list)
- type
- valuesrules

Examples
--------

Vars to be validated

.. code-block:: yaml

    vlans:
      - name: test600
        id: 600
      - name: test4094
        id: 2000

Schema to validate vars

.. code-block:: yaml

    vlans_schema:
      type: list
      schema:
        type: dict
        require_all: True
        schema:
          name:
            type: string
            regex: '^[a-z0-9]+$'
            maxlength: 10
          id:
            type: integer
            min: 1
            max: 3000

Jinja2 template

.. code-block:: jinja

    {% for vlan in vlans | gmoisio.ale.validate(vlans_schema) %}
    vlan {{ vlan.id }} admin-state enable name {{ vlan.name }}
    {% endfor %}

Vars to be validated

.. code-block:: yaml

    vlans:
      - name: test600
        id: 600
      - name: test4094
        id: 2000
    ntp_servers:
      - 0.fr.pool.ntp.org
      - 1.fr.pool.ntp.org
      - 2.fr.pool.ntp.org
      - 3.fr.pool.ntp.org

Schema to validate vars

.. code-block:: yaml

    vlans_schema:
      type: list
      schema:
        type: dict
        require_all: True
        schema:
          name:
            type: string
            regex: '^[a-z0-9]+$'
            maxlength: 10
          id:
            type: integer
            min: 1
            max: 3000
    ntp_servers_schema:
      type: list
      schema:
        regex: '^[0-3]\.fr\.pool\.ntp\.org$'

Ansible task

.. code-block:: yaml

    - name: Validate Source of Truth
      ansible.builtin.assert:
        that :
          - hostvars[inventory_hostname]['vlans'] | gmoisio.ale.validate(vlans_schema, True)
          - hostvars[inventory_hostname]['ntp_servers'] | gmoisio.ale.validate(ntp_servers_schema, True)

Authors
~~~~~~~

- Gilbert MOISIO