
# FilterPredicateValueLong

`tb_paas_client.models.FilterPredicateValueLong`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **default_value** | **int** |  | [optional] |
| **user_value** | **int** |  | [optional] |
| **dynamic_value** | [**DynamicValueLong**](DynamicValueLong.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.default_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `FilterPredicateValueLong.model_validate(data)` or `FilterPredicateValueLong.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

