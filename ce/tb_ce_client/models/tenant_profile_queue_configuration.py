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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.processing_strategy import ProcessingStrategy
from tb_ce_client.models.submit_strategy import SubmitStrategy
from typing import Optional, Set
from typing_extensions import Self

class TenantProfileQueueConfiguration(BaseModel):
    """
    TenantProfileQueueConfiguration
    """ # noqa: E501
    name: Optional[StrictStr] = None
    topic: Optional[StrictStr] = None
    poll_interval: Optional[StrictInt] = Field(default=None, alias="pollInterval")
    partitions: Optional[StrictInt] = None
    consumer_per_partition: Optional[StrictBool] = Field(default=None, alias="consumerPerPartition")
    pack_processing_timeout: Optional[StrictInt] = Field(default=None, alias="packProcessingTimeout")
    submit_strategy: Optional[SubmitStrategy] = Field(default=None, alias="submitStrategy")
    processing_strategy: Optional[ProcessingStrategy] = Field(default=None, alias="processingStrategy")
    additional_info: Optional[Any] = Field(default=None, alias="additionalInfo")
    __properties: ClassVar[List[str]] = ["name", "topic", "pollInterval", "partitions", "consumerPerPartition", "packProcessingTimeout", "submitStrategy", "processingStrategy", "additionalInfo"]

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
        """Create an instance of TenantProfileQueueConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of submit_strategy
        if self.submit_strategy:
            _dict['submitStrategy'] = self.submit_strategy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of processing_strategy
        if self.processing_strategy:
            _dict['processingStrategy'] = self.processing_strategy.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantProfileQueueConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "topic": obj.get("topic"),
            "pollInterval": obj.get("pollInterval"),
            "partitions": obj.get("partitions"),
            "consumerPerPartition": obj.get("consumerPerPartition"),
            "packProcessingTimeout": obj.get("packProcessingTimeout"),
            "submitStrategy": SubmitStrategy.from_dict(obj["submitStrategy"]) if obj.get("submitStrategy") is not None else None,
            "processingStrategy": ProcessingStrategy.from_dict(obj["processingStrategy"]) if obj.get("processingStrategy") is not None else None,
            "additionalInfo": obj.get("additionalInfo")
        })
        return _obj


