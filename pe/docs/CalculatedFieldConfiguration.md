
# CalculatedFieldConfiguration

`tb_pe_client.models.CalculatedFieldConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **output** | [**Output**](Output.md) |  | [optional] |
| **type** | **str** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.output`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CalculatedFieldConfiguration.model_validate(data)` or `CalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

