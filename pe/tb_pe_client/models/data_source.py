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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.alarm_filter_config import AlarmFilterConfig
from tb_pe_client.models.data_key import DataKey
from tb_pe_client.models.data_source_type import DataSourceType
from typing import Optional, Set
from typing_extensions import Self

class DataSource(BaseModel):
    """
    DataSource
    """ # noqa: E501
    type: Optional[DataSourceType] = None
    device_id: Optional[StrictStr] = Field(default=None, serialization_alias="deviceId")
    entity_alias_id: Optional[StrictStr] = Field(default=None, serialization_alias="entityAliasId")
    filter_id: Optional[StrictStr] = Field(default=None, serialization_alias="filterId")
    data_keys: Optional[List[DataKey]] = Field(default=None, serialization_alias="dataKeys")
    latest_data_keys: Optional[List[DataKey]] = Field(default=None, serialization_alias="latestDataKeys")
    alarm_filter_config: Optional[AlarmFilterConfig] = Field(default=None, serialization_alias="alarmFilterConfig")
    __properties: ClassVar[List[str]] = ["type", "deviceId", "entityAliasId", "filterId", "dataKeys", "latestDataKeys", "alarmFilterConfig"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data_keys (list)
        _items = []
        if self.data_keys:
            for _item_data_keys in self.data_keys:
                if _item_data_keys:
                    _items.append(_item_data_keys.to_dict())
            _dict['dataKeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in latest_data_keys (list)
        _items = []
        if self.latest_data_keys:
            for _item_latest_data_keys in self.latest_data_keys:
                if _item_latest_data_keys:
                    _items.append(_item_latest_data_keys.to_dict())
            _dict['latestDataKeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of alarm_filter_config
        if self.alarm_filter_config:
            _dict['alarmFilterConfig'] = self.alarm_filter_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "device_id": obj.get("deviceId"),
            "entity_alias_id": obj.get("entityAliasId"),
            "filter_id": obj.get("filterId"),
            "data_keys": [DataKey.from_dict(_item) for _item in obj["dataKeys"]] if obj.get("dataKeys") is not None else None,
            "latest_data_keys": [DataKey.from_dict(_item) for _item in obj["latestDataKeys"]] if obj.get("latestDataKeys") is not None else None,
            "alarm_filter_config": AlarmFilterConfig.from_dict(obj["alarmFilterConfig"]) if obj.get("alarmFilterConfig") is not None else None
        })
        return _obj


