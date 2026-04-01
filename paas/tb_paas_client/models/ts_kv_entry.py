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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.data_type import DataType
from typing import Optional, Set
from typing_extensions import Self

class TsKvEntry(BaseModel):
    """
    TsKvEntry
    """ # noqa: E501
    ts: Optional[StrictInt] = None
    value: Optional[Any] = None
    key: Optional[StrictStr] = None
    double_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, serialization_alias="doubleValue")
    long_value: Optional[StrictInt] = Field(default=None, serialization_alias="longValue")
    boolean_value: Optional[StrictBool] = Field(default=None, serialization_alias="booleanValue")
    value_as_string: Optional[StrictStr] = Field(default=None, serialization_alias="valueAsString")
    data_type: Optional[DataType] = Field(default=None, serialization_alias="dataType")
    json_value: Optional[StrictStr] = Field(default=None, serialization_alias="jsonValue")
    str_value: Optional[StrictStr] = Field(default=None, serialization_alias="strValue")
    version: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["ts", "value", "key", "doubleValue", "longValue", "booleanValue", "valueAsString", "dataType", "jsonValue", "strValue", "version"]

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
            "double_value": obj.get("doubleValue"),
            "long_value": obj.get("longValue"),
            "boolean_value": obj.get("booleanValue"),
            "value_as_string": obj.get("valueAsString"),
            "data_type": obj.get("dataType"),
            "json_value": obj.get("jsonValue"),
            "str_value": obj.get("strValue"),
            "version": obj.get("version")
        })
        return _obj


