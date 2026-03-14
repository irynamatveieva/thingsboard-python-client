
# EntityGroupInfoOwnerIdsInner

`tb_paas_client.models.EntityGroupInfoOwnerIdsInner`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **UUID** | ID of the entity, time-based UUID v1 | |
| **entity_type** | [**EntityType**](EntityType.md) |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityGroupInfoOwnerIdsInner.model_validate(data)` or `EntityGroupInfoOwnerIdsInner.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

