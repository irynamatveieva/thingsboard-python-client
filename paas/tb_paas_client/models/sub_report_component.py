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

from pydantic import ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.data_source import DataSource
from tb_paas_client.models.report_component import ReportComponent
from tb_paas_client.models.report_component_sub_type import ReportComponentSubType
from tb_paas_client.models.report_component_type import ReportComponentType
from tb_paas_client.models.report_template_id import ReportTemplateId
from typing import Optional, Set
from typing_extensions import Self

class SubReportComponent(ReportComponent):
    """
    SubReportComponent
    """ # noqa: E501
    data_sources: Optional[List[DataSource]] = Field(default=None, alias="dataSources")
    template_id: Optional[ReportTemplateId] = Field(default=None, alias="templateId")
    avoid_page_break_inside: Optional[StrictBool] = Field(default=None, alias="avoidPageBreakInside")
    __properties: ClassVar[List[str]] = ["type", "subType", "dataSources", "templateId", "avoidPageBreakInside"]

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
        """Create an instance of SubReportComponent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data_sources (list)
        _items = []
        if self.data_sources:
            for _item_data_sources in self.data_sources:
                if _item_data_sources:
                    _items.append(_item_data_sources.to_dict())
            _dict['dataSources'] = _items
        # override the default output from pydantic by calling `to_dict()` of template_id
        if self.template_id:
            _dict['templateId'] = self.template_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubReportComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "subType": obj.get("subType"),
            "dataSources": [DataSource.from_dict(_item) for _item in obj["dataSources"]] if obj.get("dataSources") is not None else None,
            "templateId": ReportTemplateId.from_dict(obj["templateId"]) if obj.get("templateId") is not None else None,
            "avoidPageBreakInside": obj.get("avoidPageBreakInside")
        })
        return _obj


