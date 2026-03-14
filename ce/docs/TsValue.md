
# TsValue

`tb_ce_client.models.TsValue`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **ts** | **int** |  | [optional] |
| **value** | **str** |  | [optional] |
| **count** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.ts`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TsValue.model_validate(data)` or `TsValue.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

