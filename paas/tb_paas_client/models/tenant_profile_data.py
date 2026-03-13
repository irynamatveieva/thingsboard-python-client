#
# Copyright 2026 ThingsBoard, Inc.
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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.tenant_profile_configuration import TenantProfileConfiguration
from tb_paas_client.models.tenant_profile_queue_configuration import TenantProfileQueueConfiguration
from typing import Optional, Set
from typing_extensions import Self

class TenantProfileData(BaseModel):
    """
    TenantProfileData
    """ # noqa: E501
    configuration: Optional[TenantProfileConfiguration] = Field(default=None, description="Complex JSON object that contains profile settings: max devices, max assets, rate limits, etc.")
    queue_configuration: Optional[List[TenantProfileQueueConfiguration]] = Field(default=None, description="JSON array of queue configuration per tenant profile", alias="queueConfiguration")
    __properties: ClassVar[List[str]] = ["configuration", "queueConfiguration"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TenantProfileData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in queue_configuration (list)
        _items = []
        if self.queue_configuration:
            for _item_queue_configuration in self.queue_configuration:
                if _item_queue_configuration:
                    _items.append(_item_queue_configuration.to_dict())
            _dict['queueConfiguration'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantProfileData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configuration": TenantProfileConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "queueConfiguration": [TenantProfileQueueConfiguration.from_dict(_item) for _item in obj["queueConfiguration"]] if obj.get("queueConfiguration") is not None else None
        })
        return _obj


