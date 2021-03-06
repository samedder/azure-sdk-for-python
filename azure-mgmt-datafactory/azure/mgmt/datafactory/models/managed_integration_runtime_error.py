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


class ManagedIntegrationRuntimeError(Model):
    """Error definition for managed integration runtime.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar time: The time when the error occurred.
    :vartype time: datetime
    :ivar code: Error code.
    :vartype code: str
    :ivar parameters: Managed integration runtime error parameters.
    :vartype parameters: list[str]
    :ivar message: Error message.
    :vartype message: str
    """

    _validation = {
        'time': {'readonly': True},
        'code': {'readonly': True},
        'parameters': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'time': {'key': 'time', 'type': 'iso-8601'},
        'code': {'key': 'code', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[str]'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self):
        self.time = None
        self.code = None
        self.parameters = None
        self.message = None
