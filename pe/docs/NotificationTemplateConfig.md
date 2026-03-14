
# NotificationTemplateConfig

`tb_pe_client.models.NotificationTemplateConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **delivery_methods_templates** | [**Dict[str, DeliveryMethodNotificationTemplate]**](DeliveryMethodNotificationTemplate.md) |  | |
| **attach_report** | **bool** |  | [optional] |
| **report_template_id** | [**ReportTemplateId**](ReportTemplateId.md) |  | [optional] |
| **user_id** | [**UserId**](UserId.md) |  | [optional] |
| **timezone** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.delivery_methods_templates`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationTemplateConfig.model_validate(data)` or `NotificationTemplateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

