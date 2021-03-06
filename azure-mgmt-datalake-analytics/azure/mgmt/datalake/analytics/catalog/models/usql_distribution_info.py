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


class USqlDistributionInfo(Model):
    """A Data Lake Analytics catalog U-SQL distribution information object.

    :param type: the type of this distribution.
    :type type: int
    :param keys: the list of directed columns in the distribution
    :type keys:
     list[~azure.mgmt.datalake.analytics.catalog.models.USqlDirectedColumn]
    :param count: the count of indices using this distribution.
    :type count: int
    :param dynamic_count: the dynamic count of indices using this
     distribution.
    :type dynamic_count: int
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'int'},
        'keys': {'key': 'keys', 'type': '[USqlDirectedColumn]'},
        'count': {'key': 'count', 'type': 'int'},
        'dynamic_count': {'key': 'dynamicCount', 'type': 'int'},
    }

    def __init__(self, type=None, keys=None, count=None, dynamic_count=None):
        super(USqlDistributionInfo, self).__init__()
        self.type = type
        self.keys = keys
        self.count = count
        self.dynamic_count = dynamic_count
