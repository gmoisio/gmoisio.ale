********************
gmoisio.ale.validate
********************

.. contents::
    :local:
    :depth: 1


Synopsis
--------
- This filter allows to validate vars against YAML schemas.
- Jinja2 template stops with an error when the vars do not conform to the schema.

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
      required: True
      type: list
      schema:
        type: dict
        schema:
          name:
            required: True
            type: string
            regex: '^[a-z0-9]+$'
            maxlength: 10
          id:
            required: True
            type: number
            min: 1
            max: 3000

.. code-block:: jinja

    {% for vlan in vlans | gmoisio.ale.validate(vlans_schema) %}
    vlan {{ vlan.id }} admin-state enable name {{ vlan.name }}
    {% endfor %}

Authors
~~~~~~~

- Gilbert MOISIO