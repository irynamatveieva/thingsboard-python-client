
# Output

`tb_paas_client.models.Output`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name** | **str** |  | [optional] |
| **scope** | [**AttributeScope**](AttributeScope.md) |  | [optional] |
| **decimals_by_default** | **int** |  | [optional] |
| **strategy** | **object** |  | [optional] |
| **type** | **str** |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Output.model_validate(data)` or `Output.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

