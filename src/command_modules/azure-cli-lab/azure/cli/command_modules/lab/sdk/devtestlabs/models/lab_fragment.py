# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .resource import Resource


class LabFragment(Resource):
    """A lab.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    :param lab_storage_type: Type of storage used by the lab. It can be either
     Premium or Standard. Default is Premium. Possible values include:
     'Standard', 'Premium'
    :type lab_storage_type: str or :class:`StorageType
     <devtestlabs.models.StorageType>`
    :param premium_data_disks: The setting to enable usage of premium data
     disks.
     When its value is 'Enabled', creation of standard or premium data disks is
     allowed.
     When its value is 'Disabled', only creation of standard data disks is
     allowed. Possible values include: 'Disabled', 'Enabled'
    :type premium_data_disks: str or :class:`PremiumDataDisk
     <devtestlabs.models.PremiumDataDisk>`
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :type unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'lab_storage_type': {'key': 'properties.labStorageType', 'type': 'str'},
        'premium_data_disks': {'key': 'properties.premiumDataDisks', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, location=None, tags=None, lab_storage_type=None, premium_data_disks=None, provisioning_state=None, unique_identifier=None):
        super(LabFragment, self).__init__(location=location, tags=tags)
        self.lab_storage_type = lab_storage_type
        self.premium_data_disks = premium_data_disks
        self.provisioning_state = provisioning_state
        self.unique_identifier = unique_identifier