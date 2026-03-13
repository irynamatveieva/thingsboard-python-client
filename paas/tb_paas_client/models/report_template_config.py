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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.entity_alias import EntityAlias
from tb_paas_client.models.filter import Filter
from tb_paas_client.models.report_component import ReportComponent
from tb_paas_client.models.tb_report_format import TbReportFormat
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_paas_client.models.csv_report_template_config import CsvReportTemplateConfig
    from tb_paas_client.models.pdf_report_template_config import PdfReportTemplateConfig

class ReportTemplateConfig(BaseModel):
    """
    ReportTemplateConfig
    """ # noqa: E501
    format: TbReportFormat = Field(description="Report format")
    entity_aliases: Optional[List[EntityAlias]] = Field(default=None, alias="entityAliases")
    filters: Optional[List[Filter]] = None
    name_pattern: Optional[StrictStr] = Field(default=None, alias="namePattern")
    components: Optional[List[ReportComponent]] = None
    time_data_pattern: Optional[StrictStr] = Field(default=None, alias="timeDataPattern")
    __properties: ClassVar[List[str]] = ["format", "entityAliases", "filters", "namePattern", "components", "timeDataPattern"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'format'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'CSV': 'CsvReportTemplateConfig','PDF': 'PdfReportTemplateConfig'
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
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[CsvReportTemplateConfig, PdfReportTemplateConfig]]:
        """Create an instance of ReportTemplateConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entity_aliases (list)
        _items = []
        if self.entity_aliases:
            for _item_entity_aliases in self.entity_aliases:
                if _item_entity_aliases:
                    _items.append(_item_entity_aliases.to_dict())
            _dict['entityAliases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item_filters in self.filters:
                if _item_filters:
                    _items.append(_item_filters.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[CsvReportTemplateConfig, PdfReportTemplateConfig]]:
        """Create an instance of ReportTemplateConfig from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'CsvReportTemplateConfig':
            return import_module("tb_paas_client.models.csv_report_template_config").CsvReportTemplateConfig.from_dict(obj)
        if object_type ==  'PdfReportTemplateConfig':
            return import_module("tb_paas_client.models.pdf_report_template_config").PdfReportTemplateConfig.from_dict(obj)

        raise ValueError("ReportTemplateConfig failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


