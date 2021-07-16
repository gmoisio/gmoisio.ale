from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from cerberus import Validator


def validate(vars, data_schema):
    if not vars:
        raise AnsibleFilterError(
            'Vars list is empty, nothing to validate!')
    if not data_schema:
        raise AnsibleFilterError(
            'The schema dictionary is empty, cannot validate!')
    v = Validator()
    try:
        v.validate({'schema': vars}, {'schema': data_schema})
    except Exception as e:
        raise AnsibleFilterError(e)
    if v.errors:
        raise AnsibleFilterError(v.errors)
    else:
        return vars


class FilterModule(object):

    def filters(self):
        return {
            'validate': validate
        }
