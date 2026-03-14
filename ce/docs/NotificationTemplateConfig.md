
# NotificationTemplateConfig

`tb_ce_client.models.NotificationTemplateConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **delivery_methods_templates** | [**Dict[str, DeliveryMethodNotificationTemplate]**](DeliveryMethodNotificationTemplate.md) |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.delivery_methods_templates`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationTemplateConfig.model_validate(data)` or `NotificationTemplateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

