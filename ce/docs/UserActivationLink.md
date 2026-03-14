
# UserActivationLink

`tb_ce_client.models.UserActivationLink`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **value** | **str** |  | [optional] |
| **ttl_ms** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserActivationLink.model_validate(data)` or `UserActivationLink.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

