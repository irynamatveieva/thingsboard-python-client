
# MicrosoftTeamsDeliveryMethodNotificationTemplate

`tb_pe_client.models.MicrosoftTeamsDeliveryMethodNotificationTemplate`

**Extends:** **DeliveryMethodNotificationTemplate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **subject** | **str** |  | [optional] |
| **theme_color** | **str** |  | [optional] |
| **button** | [**Button**](Button.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.subject`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MicrosoftTeamsDeliveryMethodNotificationTemplate.model_validate(data)` or `MicrosoftTeamsDeliveryMethodNotificationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

