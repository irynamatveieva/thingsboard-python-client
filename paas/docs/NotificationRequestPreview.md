
# NotificationRequestPreview

`tb_paas_client.models.NotificationRequestPreview`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **processed_templates** | [**Dict[str, DeliveryMethodNotificationTemplate]**](DeliveryMethodNotificationTemplate.md) |  | [optional] |
| **total_recipients_count** | **int** |  | [optional] |
| **recipients_count_by_target** | **Dict[str, int]** |  | [optional] |
| **recipients_preview** | **List[str]** |  | [optional] |



## Referenced Types

#### DeliveryMethodNotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| body | str |  |  |
| method | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.processed_templates`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRequestPreview.model_validate(data)` or `NotificationRequestPreview.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

