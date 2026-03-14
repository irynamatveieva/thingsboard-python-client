
# KeyFilter

`tb_paas_client.models.KeyFilter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | [**EntityKey**](EntityKey.md) |  | [optional] |
| **value_type** | [**EntityKeyValueType**](EntityKeyValueType.md) |  | [optional] |
| **predicate** | [**KeyFilterPredicate**](KeyFilterPredicate.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `KeyFilter.model_validate(data)` or `KeyFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

