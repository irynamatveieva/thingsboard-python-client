
# ReportJobConfiguration

`tb_pe_client.models.ReportJobConfiguration`

**Extends:** **JobConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **report_template_id** | [**ReportTemplateId**](ReportTemplateId.md) |  | [optional] |
| **user_id** | [**UserId**](UserId.md) |  | [optional] |
| **timezone** | **str** |  | [optional] |
| **targets** | **List[UUID]** |  | [optional] |
| **notification_template_id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | [optional] |
| **notification_requests** | [**List[NotificationRequest]**](NotificationRequest.md) |  | [optional] |
| **originator** | [**EntityId**](EntityId.md) |  | [optional] |
| **rule_node** | [**RuleNode**](RuleNode.md) |  | [optional] |
| **output_tb_msg_proto** | **str** |  | [optional] |
| **queue_name** | **str** |  | [optional] |
| **scheduler_event_info** | [**EntityInfo**](EntityInfo.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.report_template_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportJobConfiguration.model_validate(data)` or `ReportJobConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

