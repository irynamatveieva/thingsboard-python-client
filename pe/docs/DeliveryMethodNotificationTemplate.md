
# DeliveryMethodNotificationTemplate

`tb_pe_client.models.DeliveryMethodNotificationTemplate`

Base template for different delivery methods

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** |  | [optional] |
| **body** | **str** |  | |
| **method** | **str** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeliveryMethodNotificationTemplate.model_validate(data)` or `DeliveryMethodNotificationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

