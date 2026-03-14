
# EntityDataSortOrder

`tb_pe_client.models.EntityDataSortOrder`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | [**EntityKey**](EntityKey.md) |  | [optional] |
| **direction** | [**Direction**](Direction.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataSortOrder.model_validate(data)` or `EntityDataSortOrder.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

