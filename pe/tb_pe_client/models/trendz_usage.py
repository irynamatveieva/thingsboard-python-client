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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.entity import Entity
from tb_pe_client.models.simple_entity import SimpleEntity
from typing import Optional, Set
from typing_extensions import Self

class TrendzUsage(BaseModel):
    """
    TrendzUsage
    """ # noqa: E501
    used: Optional[StrictBool] = None
    anomaly_usage: Optional[Entity] = Field(default=None, alias="anomalyUsage")
    prediction_usage: Optional[Entity] = Field(default=None, alias="predictionUsage")
    calculation_usage: Optional[Entity] = Field(default=None, alias="calculationUsage")
    view_usage: Optional[SimpleEntity] = Field(default=None, alias="viewUsage")
    metric_usage: Optional[SimpleEntity] = Field(default=None, alias="metricUsage")
    chat_usage: Optional[SimpleEntity] = Field(default=None, alias="chatUsage")
    __properties: ClassVar[List[str]] = ["used", "anomalyUsage", "predictionUsage", "calculationUsage", "viewUsage", "metricUsage", "chatUsage"]

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
        """Create an instance of TrendzUsage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of anomaly_usage
        if self.anomaly_usage:
            _dict['anomalyUsage'] = self.anomaly_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prediction_usage
        if self.prediction_usage:
            _dict['predictionUsage'] = self.prediction_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of calculation_usage
        if self.calculation_usage:
            _dict['calculationUsage'] = self.calculation_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of view_usage
        if self.view_usage:
            _dict['viewUsage'] = self.view_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric_usage
        if self.metric_usage:
            _dict['metricUsage'] = self.metric_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_usage
        if self.chat_usage:
            _dict['chatUsage'] = self.chat_usage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrendzUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "used": obj.get("used"),
            "anomalyUsage": Entity.from_dict(obj["anomalyUsage"]) if obj.get("anomalyUsage") is not None else None,
            "predictionUsage": Entity.from_dict(obj["predictionUsage"]) if obj.get("predictionUsage") is not None else None,
            "calculationUsage": Entity.from_dict(obj["calculationUsage"]) if obj.get("calculationUsage") is not None else None,
            "viewUsage": SimpleEntity.from_dict(obj["viewUsage"]) if obj.get("viewUsage") is not None else None,
            "metricUsage": SimpleEntity.from_dict(obj["metricUsage"]) if obj.get("metricUsage") is not None else None,
            "chatUsage": SimpleEntity.from_dict(obj["chatUsage"]) if obj.get("chatUsage") is not None else None
        })
        return _obj


