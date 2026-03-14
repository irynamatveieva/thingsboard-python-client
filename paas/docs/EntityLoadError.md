
# EntityLoadError

`tb_paas_client.models.EntityLoadError`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | [optional] |
| **source** | [**EntityId**](EntityId.md) |  | [optional] |
| **target** | [**EntityId**](EntityId.md) |  | [optional] |
| **message** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityLoadError.model_validate(data)` or `EntityLoadError.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

