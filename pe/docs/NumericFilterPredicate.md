
# NumericFilterPredicate

`tb_pe_client.models.NumericFilterPredicate`

**Extends:** **KeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**NumericOperation**](NumericOperation.md) |  | [optional] |
| **value** | [**FilterPredicateValueDouble**](FilterPredicateValueDouble.md) | The value associated with the filter predicate | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NumericFilterPredicate.model_validate(data)` or `NumericFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

