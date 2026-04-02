
# RelationPathLevel

`tb_ce_client.models.RelationPathLevel`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **direction** | [**EntitySearchDirection**](EntitySearchDirection.md) |  | |
| **relation_type** | **str** |  | |



## Referenced Types

#### EntitySearchDirection (enum)
`FROM` | `TO`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.direction`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelationPathLevel.model_validate(data)` or `RelationPathLevel.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

