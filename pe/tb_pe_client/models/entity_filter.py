#
# Copyright © 2026-2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_pe_client.models.api_usage_state_filter import ApiUsageStateFilter
    from tb_pe_client.models.asset_search_query_filter import AssetSearchQueryFilter
    from tb_pe_client.models.asset_type_filter import AssetTypeFilter
    from tb_pe_client.models.device_search_query_filter import DeviceSearchQueryFilter
    from tb_pe_client.models.device_type_filter import DeviceTypeFilter
    from tb_pe_client.models.edge_search_query_filter import EdgeSearchQueryFilter
    from tb_pe_client.models.edge_type_filter import EdgeTypeFilter
    from tb_pe_client.models.entities_by_group_name_filter import EntitiesByGroupNameFilter
    from tb_pe_client.models.entity_group_filter import EntityGroupFilter
    from tb_pe_client.models.entity_group_list_filter import EntityGroupListFilter
    from tb_pe_client.models.entity_group_name_filter import EntityGroupNameFilter
    from tb_pe_client.models.entity_list_filter import EntityListFilter
    from tb_pe_client.models.entity_name_filter import EntityNameFilter
    from tb_pe_client.models.entity_type_filter import EntityTypeFilter
    from tb_pe_client.models.entity_view_search_query_filter import EntityViewSearchQueryFilter
    from tb_pe_client.models.entity_view_type_filter import EntityViewTypeFilter
    from tb_pe_client.models.relations_query_filter import RelationsQueryFilter
    from tb_pe_client.models.scheduler_event_filter import SchedulerEventFilter
    from tb_pe_client.models.single_entity_filter import SingleEntityFilter
    from tb_pe_client.models.state_entity_filter import StateEntityFilter
    from tb_pe_client.models.state_entity_owner_filter import StateEntityOwnerFilter

class EntityFilter(BaseModel):
    """
    Filter for selecting entities
    """ # noqa: E501
    type: StrictStr
    __properties: ClassVar[List[str]] = ["type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'apiUsageState': 'ApiUsageStateFilter','assetSearchQuery': 'AssetSearchQueryFilter','assetType': 'AssetTypeFilter','deviceSearchQuery': 'DeviceSearchQueryFilter','deviceType': 'DeviceTypeFilter','edgeSearchQuery': 'EdgeSearchQueryFilter','edgeType': 'EdgeTypeFilter','entitiesByGroupName': 'EntitiesByGroupNameFilter','entityGroup': 'EntityGroupFilter','entityGroupList': 'EntityGroupListFilter','entityGroupName': 'EntityGroupNameFilter','entityList': 'EntityListFilter','entityName': 'EntityNameFilter','entityType': 'EntityTypeFilter','entityViewSearchQuery': 'EntityViewSearchQueryFilter','entityViewType': 'EntityViewTypeFilter','relationsQuery': 'RelationsQueryFilter','schedulerEvent': 'SchedulerEventFilter','singleEntity': 'SingleEntityFilter','stateEntity': 'StateEntityFilter','stateEntityOwner': 'StateEntityOwnerFilter'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.model_dump(by_alias=False, mode='json'))

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[ApiUsageStateFilter, AssetSearchQueryFilter, AssetTypeFilter, DeviceSearchQueryFilter, DeviceTypeFilter, EdgeSearchQueryFilter, EdgeTypeFilter, EntitiesByGroupNameFilter, EntityGroupFilter, EntityGroupListFilter, EntityGroupNameFilter, EntityListFilter, EntityNameFilter, EntityTypeFilter, EntityViewSearchQueryFilter, EntityViewTypeFilter, RelationsQueryFilter, SchedulerEventFilter, SingleEntityFilter, StateEntityFilter, StateEntityOwnerFilter]]:
        """Create an instance of EntityFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[ApiUsageStateFilter, AssetSearchQueryFilter, AssetTypeFilter, DeviceSearchQueryFilter, DeviceTypeFilter, EdgeSearchQueryFilter, EdgeTypeFilter, EntitiesByGroupNameFilter, EntityGroupFilter, EntityGroupListFilter, EntityGroupNameFilter, EntityListFilter, EntityNameFilter, EntityTypeFilter, EntityViewSearchQueryFilter, EntityViewTypeFilter, RelationsQueryFilter, SchedulerEventFilter, SingleEntityFilter, StateEntityFilter, StateEntityOwnerFilter]]:
        """Create an instance of EntityFilter from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'ApiUsageStateFilter':
            return import_module("tb_pe_client.models.api_usage_state_filter").ApiUsageStateFilter.from_dict(obj)
        if object_type ==  'AssetSearchQueryFilter':
            return import_module("tb_pe_client.models.asset_search_query_filter").AssetSearchQueryFilter.from_dict(obj)
        if object_type ==  'AssetTypeFilter':
            return import_module("tb_pe_client.models.asset_type_filter").AssetTypeFilter.from_dict(obj)
        if object_type ==  'DeviceSearchQueryFilter':
            return import_module("tb_pe_client.models.device_search_query_filter").DeviceSearchQueryFilter.from_dict(obj)
        if object_type ==  'DeviceTypeFilter':
            return import_module("tb_pe_client.models.device_type_filter").DeviceTypeFilter.from_dict(obj)
        if object_type ==  'EdgeSearchQueryFilter':
            return import_module("tb_pe_client.models.edge_search_query_filter").EdgeSearchQueryFilter.from_dict(obj)
        if object_type ==  'EdgeTypeFilter':
            return import_module("tb_pe_client.models.edge_type_filter").EdgeTypeFilter.from_dict(obj)
        if object_type ==  'EntitiesByGroupNameFilter':
            return import_module("tb_pe_client.models.entities_by_group_name_filter").EntitiesByGroupNameFilter.from_dict(obj)
        if object_type ==  'EntityGroupFilter':
            return import_module("tb_pe_client.models.entity_group_filter").EntityGroupFilter.from_dict(obj)
        if object_type ==  'EntityGroupListFilter':
            return import_module("tb_pe_client.models.entity_group_list_filter").EntityGroupListFilter.from_dict(obj)
        if object_type ==  'EntityGroupNameFilter':
            return import_module("tb_pe_client.models.entity_group_name_filter").EntityGroupNameFilter.from_dict(obj)
        if object_type ==  'EntityListFilter':
            return import_module("tb_pe_client.models.entity_list_filter").EntityListFilter.from_dict(obj)
        if object_type ==  'EntityNameFilter':
            return import_module("tb_pe_client.models.entity_name_filter").EntityNameFilter.from_dict(obj)
        if object_type ==  'EntityTypeFilter':
            return import_module("tb_pe_client.models.entity_type_filter").EntityTypeFilter.from_dict(obj)
        if object_type ==  'EntityViewSearchQueryFilter':
            return import_module("tb_pe_client.models.entity_view_search_query_filter").EntityViewSearchQueryFilter.from_dict(obj)
        if object_type ==  'EntityViewTypeFilter':
            return import_module("tb_pe_client.models.entity_view_type_filter").EntityViewTypeFilter.from_dict(obj)
        if object_type ==  'RelationsQueryFilter':
            return import_module("tb_pe_client.models.relations_query_filter").RelationsQueryFilter.from_dict(obj)
        if object_type ==  'SchedulerEventFilter':
            return import_module("tb_pe_client.models.scheduler_event_filter").SchedulerEventFilter.from_dict(obj)
        if object_type ==  'SingleEntityFilter':
            return import_module("tb_pe_client.models.single_entity_filter").SingleEntityFilter.from_dict(obj)
        if object_type ==  'StateEntityFilter':
            return import_module("tb_pe_client.models.state_entity_filter").StateEntityFilter.from_dict(obj)
        if object_type ==  'StateEntityOwnerFilter':
            return import_module("tb_pe_client.models.state_entity_owner_filter").StateEntityOwnerFilter.from_dict(obj)

        raise ValueError("EntityFilter failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


