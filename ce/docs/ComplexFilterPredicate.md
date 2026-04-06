
# ComplexFilterPredicate

`tb_ce_client.models.ComplexFilterPredicate`

**Extends:** **KeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**ComplexOperation**](ComplexOperation.md) |  | [optional] |
| **predicates** | [**List[KeyFilterPredicate]**](KeyFilterPredicate.md) |  | [optional] |



## Referenced Types

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### ComplexOperation (enum)
`AND` | `OR`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ComplexFilterPredicate.model_validate(data)` or `ComplexFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

