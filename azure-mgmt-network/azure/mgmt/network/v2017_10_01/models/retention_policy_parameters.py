# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RetentionPolicyParameters(Model):
    """Parameters that define the retention policy for flow log.

    :param days: Number of days to retain flow log records. Default value: 0 .
    :type days: int
    :param enabled: Flag to enable/disable retention. Default value: False .
    :type enabled: bool
    """

    _attribute_map = {
        'days': {'key': 'days', 'type': 'int'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(self, days=0, enabled=False):
        super(RetentionPolicyParameters, self).__init__()
        self.days = days
        self.enabled = enabled
