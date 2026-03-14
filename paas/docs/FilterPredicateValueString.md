
# FilterPredicateValueString

`tb_paas_client.models.FilterPredicateValueString`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **default_value** | **str** |  | [optional] |
| **user_value** | **str** |  | [optional] |
| **dynamic_value** | [**DynamicValueString**](DynamicValueString.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.default_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `FilterPredicateValueString.model_validate(data)` or `FilterPredicateValueString.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

