
# BooleanFilterPredicate

`tb_paas_client.models.BooleanFilterPredicate`

**Extends:** **KeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**BooleanOperation**](BooleanOperation.md) |  | [optional] |
| **value** | [**FilterPredicateValueBoolean**](FilterPredicateValueBoolean.md) | The value associated with the filter predicate | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BooleanFilterPredicate.model_validate(data)` or `BooleanFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

