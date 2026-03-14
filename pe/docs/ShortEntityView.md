
# ShortEntityView

`tb_pe_client.models.ShortEntityView`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EntityId**](EntityId.md) | Entity Id object | [readonly] |
| **name** | **str** | Name of the entity | [readonly] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ShortEntityView.model_validate(data)` or `ShortEntityView.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

