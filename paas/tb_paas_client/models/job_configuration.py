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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from tb_paas_client.models.task_result import TaskResult
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_paas_client.models.cf_reprocessing_job_configuration import CfReprocessingJobConfiguration
    from tb_paas_client.models.dummy_job_configuration import DummyJobConfiguration
    from tb_paas_client.models.report_job_configuration import ReportJobConfiguration

class JobConfiguration(BaseModel):
    """
    JobConfiguration
    """ # noqa: E501
    tasks_key: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="tasksKey")
    to_reprocess: Optional[List[TaskResult]] = Field(default=None, alias="toReprocess")
    type: StrictStr
    __properties: ClassVar[List[str]] = ["tasksKey", "toReprocess", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'CF_REPROCESSING': 'CfReprocessingJobConfiguration','DUMMY': 'DummyJobConfiguration','REPORT': 'ReportJobConfiguration'
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
    def from_json(cls, json_str: str) -> Optional[Union[CfReprocessingJobConfiguration, DummyJobConfiguration, ReportJobConfiguration]]:
        """Create an instance of JobConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in to_reprocess (list)
        _items = []
        if self.to_reprocess:
            for _item_to_reprocess in self.to_reprocess:
                if _item_to_reprocess:
                    _items.append(_item_to_reprocess.to_dict())
            _dict['toReprocess'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[CfReprocessingJobConfiguration, DummyJobConfiguration, ReportJobConfiguration]]:
        """Create an instance of JobConfiguration from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'CfReprocessingJobConfiguration':
            return import_module("tb_paas_client.models.cf_reprocessing_job_configuration").CfReprocessingJobConfiguration.from_dict(obj)
        if object_type ==  'DummyJobConfiguration':
            return import_module("tb_paas_client.models.dummy_job_configuration").DummyJobConfiguration.from_dict(obj)
        if object_type ==  'ReportJobConfiguration':
            return import_module("tb_paas_client.models.report_job_configuration").ReportJobConfiguration.from_dict(obj)

        raise ValueError("JobConfiguration failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


