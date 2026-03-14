
# FilterPredicateValueBoolean

`tb_pe_client.models.FilterPredicateValueBoolean`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **default_value** | **bool** |  | [optional] |
| **user_value** | **bool** |  | [optional] |
| **dynamic_value** | [**DynamicValueBoolean**](DynamicValueBoolean.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.default_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `FilterPredicateValueBoolean.model_validate(data)` or `FilterPredicateValueBoolean.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

