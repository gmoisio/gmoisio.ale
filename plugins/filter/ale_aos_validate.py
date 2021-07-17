#!/usr/bin/env python

# Copyright (c) 2021, Gilbert MOISIO
#
# All rights reserved.
#
# License: CC BY-NC-ND 4.0
#          Attribution-NonCommercial-NoDerivatives 4.0 International
#
# You are free to:
#
# Share — copy and redistribute the material in any medium or format
#
# Under the following terms:
#
# Attribution   — You must give appropriate credit, provide a link to the
#                 license, and indicate if changes were made. You may do so in
#                 any reasonable manner, but not in any way that suggests the
#                 licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# NoDerivatives — If you remix, transform, or build upon the material, you may
#                 not distribute the modified material.
# No additional restrictions — You may not apply legal terms or technological
#                              measures that legally restrict others from doing
#                              anything the license permits.
#

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from cerberus import Validator

'''
filter: ale_aos_validate
author: Gilbert MOISIO
version_added: "1.3.0" # of ale collection
short_description: Validate vars against schema.
description:
    - Try to validate vars against schema. It returns the vars or a boolean
      depending on the check value.
requirements:
    - cerberus >= 1.3.4
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
'''

'''
returns:

    - vars if they validate against schema and check value is False
    - error message if vars do not validate against schema and check value is False
    - boolean True if vars validate against schema and check value is True
    - boolean False if vars do not validate against schema and check value is True
'''


def validate(vars, data_schema, check=False):
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
        if check:
            return False
        else:
            raise AnsibleFilterError(v.errors)
    else:
        return True if check else vars


class FilterModule(object):

    def filters(self):
        return {
            'validate': validate
        }
