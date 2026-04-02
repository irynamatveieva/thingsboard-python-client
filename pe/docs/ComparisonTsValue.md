
# ComparisonTsValue

`tb_pe_client.models.ComparisonTsValue`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **current** | [**TsValue**](TsValue.md) |  | [optional] |
| **previous** | [**TsValue**](TsValue.md) |  | [optional] |



## Referenced Types

#### TsValue
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ts | int |  | [optional] |
| value | str |  | [optional] |
| count | int |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.current`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ComparisonTsValue.model_validate(data)` or `ComparisonTsValue.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

