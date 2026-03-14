
# ReportRequest

`tb_pe_client.models.ReportRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **report_template_id** | [**ReportTemplateId**](ReportTemplateId.md) | Json object representing the report template id. | [optional] |
| **report_template_config** | [**ReportTemplateConfig**](ReportTemplateConfig.md) | Json object representing the report template config. | [optional] |
| **timezone** | **str** | Timezone used for report generation. | [optional] |
| **user_id** | **str** | A string value representing the user id. | [optional] |
| **originator** | [**EntityId**](EntityId.md) | Json object representing the originator id. | [optional] |
| **targets** | **List[UUID]** |  | [optional] |
| **notification_template_id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.report_template_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportRequest.model_validate(data)` or `ReportRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

