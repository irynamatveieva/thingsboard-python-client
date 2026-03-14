
# StringFilterPredicate

`tb_ce_client.models.StringFilterPredicate`

**Extends:** **KeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**StringOperation**](StringOperation.md) |  | [optional] |
| **value** | [**FilterPredicateValueString**](FilterPredicateValueString.md) | The value associated with the filter predicate | [optional] |
| **ignore_case** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StringFilterPredicate.model_validate(data)` or `StringFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

