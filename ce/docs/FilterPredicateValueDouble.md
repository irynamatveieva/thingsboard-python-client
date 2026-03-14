
# FilterPredicateValueDouble

`tb_ce_client.models.FilterPredicateValueDouble`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **default_value** | **float** |  | [optional] |
| **user_value** | **float** |  | [optional] |
| **dynamic_value** | [**DynamicValueDouble**](DynamicValueDouble.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.default_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `FilterPredicateValueDouble.model_validate(data)` or `FilterPredicateValueDouble.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

