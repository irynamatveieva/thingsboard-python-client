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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.entity_info import EntityInfo
from tb_pe_client.models.job_configuration import JobConfiguration
from tb_pe_client.models.notification_request import NotificationRequest
from tb_pe_client.models.notification_template_id import NotificationTemplateId
from tb_pe_client.models.report_template_id import ReportTemplateId
from tb_pe_client.models.rule_node import RuleNode
from tb_pe_client.models.task_result import TaskResult
from tb_pe_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class ReportJobConfiguration(JobConfiguration):
    """
    ReportJobConfiguration
    """ # noqa: E501
    report_template_id: Optional[ReportTemplateId] = Field(default=None, alias="reportTemplateId")
    user_id: Optional[UserId] = Field(default=None, alias="userId")
    timezone: Optional[StrictStr] = None
    targets: Optional[List[UUID]] = None
    notification_template_id: Optional[NotificationTemplateId] = Field(default=None, alias="notificationTemplateId")
    notification_requests: Optional[List[NotificationRequest]] = Field(default=None, alias="notificationRequests")
    originator: Optional[EntityId] = None
    rule_node: Optional[RuleNode] = Field(default=None, alias="ruleNode")
    output_tb_msg_proto: Optional[StrictStr] = Field(default=None, alias="outputTbMsgProto")
    queue_name: Optional[StrictStr] = Field(default=None, alias="queueName")
    scheduler_event_info: Optional[EntityInfo] = Field(default=None, alias="schedulerEventInfo")
    __properties: ClassVar[List[str]] = ["tasksKey", "toReprocess", "type", "reportTemplateId", "userId", "timezone", "targets", "notificationTemplateId", "notificationRequests", "originator", "ruleNode", "outputTbMsgProto", "queueName", "schedulerEventInfo"]

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
        """Create an instance of ReportJobConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of report_template_id
        if self.report_template_id:
            _dict['reportTemplateId'] = self.report_template_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notification_template_id
        if self.notification_template_id:
            _dict['notificationTemplateId'] = self.notification_template_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notification_requests (list)
        _items = []
        if self.notification_requests:
            for _item_notification_requests in self.notification_requests:
                if _item_notification_requests:
                    _items.append(_item_notification_requests.to_dict())
            _dict['notificationRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of originator
        if self.originator:
            _dict['originator'] = self.originator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rule_node
        if self.rule_node:
            _dict['ruleNode'] = self.rule_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scheduler_event_info
        if self.scheduler_event_info:
            _dict['schedulerEventInfo'] = self.scheduler_event_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportJobConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tasksKey": obj.get("tasksKey"),
            "toReprocess": [TaskResult.from_dict(_item) for _item in obj["toReprocess"]] if obj.get("toReprocess") is not None else None,
            "type": obj.get("type"),
            "reportTemplateId": ReportTemplateId.from_dict(obj["reportTemplateId"]) if obj.get("reportTemplateId") is not None else None,
            "userId": UserId.from_dict(obj["userId"]) if obj.get("userId") is not None else None,
            "timezone": obj.get("timezone"),
            "targets": obj.get("targets"),
            "notificationTemplateId": NotificationTemplateId.from_dict(obj["notificationTemplateId"]) if obj.get("notificationTemplateId") is not None else None,
            "notificationRequests": [NotificationRequest.from_dict(_item) for _item in obj["notificationRequests"]] if obj.get("notificationRequests") is not None else None,
            "originator": EntityId.from_dict(obj["originator"]) if obj.get("originator") is not None else None,
            "ruleNode": RuleNode.from_dict(obj["ruleNode"]) if obj.get("ruleNode") is not None else None,
            "outputTbMsgProto": obj.get("outputTbMsgProto"),
            "queueName": obj.get("queueName"),
            "schedulerEventInfo": EntityInfo.from_dict(obj["schedulerEventInfo"]) if obj.get("schedulerEventInfo") is not None else None
        })
        return _obj


