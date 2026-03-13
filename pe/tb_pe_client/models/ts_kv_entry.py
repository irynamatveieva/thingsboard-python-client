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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_pe_client.models.data_type import DataType
from typing import Optional, Set
from typing_extensions import Self

class TsKvEntry(BaseModel):
    """
    TsKvEntry
    """ # noqa: E501
    ts: Optional[StrictInt] = None
    value: Optional[Any] = None
    key: Optional[StrictStr] = None
    double_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="doubleValue")
    long_value: Optional[StrictInt] = Field(default=None, alias="longValue")
    boolean_value: Optional[StrictBool] = Field(default=None, alias="booleanValue")
    value_as_string: Optional[StrictStr] = Field(default=None, alias="valueAsString")
    data_type: Optional[DataType] = Field(default=None, alias="dataType")
    json_value: Optional[StrictStr] = Field(default=None, alias="jsonValue")
    str_value: Optional[StrictStr] = Field(default=None, alias="strValue")
    version: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["ts", "value", "key", "doubleValue", "longValue", "booleanValue", "valueAsString", "dataType", "jsonValue", "strValue", "version"]

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
        """Create an instance of TsKvEntry from a JSON string"""
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
        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TsKvEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ts": obj.get("ts"),
            "value": obj.get("value"),
            "key": obj.get("key"),
            "doubleValue": obj.get("doubleValue"),
            "longValue": obj.get("longValue"),
            "booleanValue": obj.get("booleanValue"),
            "valueAsString": obj.get("valueAsString"),
            "dataType": obj.get("dataType"),
            "jsonValue": obj.get("jsonValue"),
            "strValue": obj.get("strValue"),
            "version": obj.get("version")
        })
        return _obj


