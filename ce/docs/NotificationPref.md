
# NotificationPref

`tb_ce_client.models.NotificationPref`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** |  | [optional] |
| **enabled_delivery_methods** | **Dict[str, bool]** |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationPref.model_validate(data)` or `NotificationPref.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

