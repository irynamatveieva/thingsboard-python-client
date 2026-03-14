
# FilterPredicateValueInteger

`tb_pe_client.models.FilterPredicateValueInteger`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **default_value** | **int** |  | [optional] |
| **user_value** | **int** |  | [optional] |
| **dynamic_value** | [**DynamicValueInteger**](DynamicValueInteger.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.default_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `FilterPredicateValueInteger.model_validate(data)` or `FilterPredicateValueInteger.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

