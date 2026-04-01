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
from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.event_type import EventType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_paas_client.models.calculated_field_debug_event_filter import CalculatedFieldDebugEventFilter
    from tb_paas_client.models.debug_converter_event_filter import DebugConverterEventFilter
    from tb_paas_client.models.debug_integration_event_filter import DebugIntegrationEventFilter
    from tb_paas_client.models.rule_chain_debug_event_filter import RuleChainDebugEventFilter
    from tb_paas_client.models.rule_node_debug_event_filter import RuleNodeDebugEventFilter
    from tb_paas_client.models.error_event_filter import ErrorEventFilter
    from tb_paas_client.models.life_cycle_event_filter import LifeCycleEventFilter
    from tb_paas_client.models.raw_data_event_filter import RawDataEventFilter
    from tb_paas_client.models.statistics_event_filter import StatisticsEventFilter

class EventFilter(BaseModel):
    """
    Filter for various event types
    """ # noqa: E501
    event_type: EventType = Field(description="String value representing the event type", serialization_alias="eventType")
    not_empty: Optional[StrictBool] = Field(default=None, serialization_alias="notEmpty")
    __properties: ClassVar[List[str]] = ["eventType", "notEmpty"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'eventType'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'DEBUG_CALCULATED_FIELD': 'CalculatedFieldDebugEventFilter','DEBUG_CONVERTER': 'DebugConverterEventFilter','DEBUG_INTEGRATION': 'DebugIntegrationEventFilter','DEBUG_RULE_CHAIN': 'RuleChainDebugEventFilter','DEBUG_RULE_NODE': 'RuleNodeDebugEventFilter','ERROR': 'ErrorEventFilter','LC_EVENT': 'LifeCycleEventFilter','RAW_DATA': 'RawDataEventFilter','STATS': 'StatisticsEventFilter'
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
    def from_json(cls, json_str: str) -> Optional[Union[CalculatedFieldDebugEventFilter, DebugConverterEventFilter, DebugIntegrationEventFilter, RuleChainDebugEventFilter, RuleNodeDebugEventFilter, ErrorEventFilter, LifeCycleEventFilter, RawDataEventFilter, StatisticsEventFilter]]:
        """Create an instance of EventFilter from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[CalculatedFieldDebugEventFilter, DebugConverterEventFilter, DebugIntegrationEventFilter, RuleChainDebugEventFilter, RuleNodeDebugEventFilter, ErrorEventFilter, LifeCycleEventFilter, RawDataEventFilter, StatisticsEventFilter]]:
        """Create an instance of EventFilter from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'CalculatedFieldDebugEventFilter':
            return import_module("tb_paas_client.models.calculated_field_debug_event_filter").CalculatedFieldDebugEventFilter.from_dict(obj)
        if object_type ==  'DebugConverterEventFilter':
            return import_module("tb_paas_client.models.debug_converter_event_filter").DebugConverterEventFilter.from_dict(obj)
        if object_type ==  'DebugIntegrationEventFilter':
            return import_module("tb_paas_client.models.debug_integration_event_filter").DebugIntegrationEventFilter.from_dict(obj)
        if object_type ==  'RuleChainDebugEventFilter':
            return import_module("tb_paas_client.models.rule_chain_debug_event_filter").RuleChainDebugEventFilter.from_dict(obj)
        if object_type ==  'RuleNodeDebugEventFilter':
            return import_module("tb_paas_client.models.rule_node_debug_event_filter").RuleNodeDebugEventFilter.from_dict(obj)
        if object_type ==  'ErrorEventFilter':
            return import_module("tb_paas_client.models.error_event_filter").ErrorEventFilter.from_dict(obj)
        if object_type ==  'LifeCycleEventFilter':
            return import_module("tb_paas_client.models.life_cycle_event_filter").LifeCycleEventFilter.from_dict(obj)
        if object_type ==  'RawDataEventFilter':
            return import_module("tb_paas_client.models.raw_data_event_filter").RawDataEventFilter.from_dict(obj)
        if object_type ==  'StatisticsEventFilter':
            return import_module("tb_paas_client.models.statistics_event_filter").StatisticsEventFilter.from_dict(obj)

        raise ValueError("EventFilter failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


