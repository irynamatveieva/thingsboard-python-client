
# EntityAlias

`tb_pe_client.models.EntityAlias`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **alias** | **str** |  | [optional] |
| **filter** | [**EntityFilter**](EntityFilter.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityAlias.model_validate(data)` or `EntityAlias.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

