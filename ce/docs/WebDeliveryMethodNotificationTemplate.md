
# WebDeliveryMethodNotificationTemplate

`tb_ce_client.models.WebDeliveryMethodNotificationTemplate`

**Extends:** **DeliveryMethodNotificationTemplate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **subject** | **str** | Subject line for the web notification | |
| **additional_config** | **object** | Additional JSON configuration for web buttons/actions | [optional] |



## Referenced Types

#### DeliveryMethodNotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| body | str |  |  |
| method | str |  |  |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.subject`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WebDeliveryMethodNotificationTemplate.model_validate(data)` or `WebDeliveryMethodNotificationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

