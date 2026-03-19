
# EntityId

`tb_pe_client.models.EntityId`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_type** | [**EntityType**](EntityType.md) |  | |
| **id** | **UUID** | ID of the entity, time-based UUID v1 | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityId.model_validate(data)` or `EntityId.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

