
# EntityTypeVersionLoadRequest

`tb_ce_client.models.EntityTypeVersionLoadRequest`

**Extends:** **VersionLoadRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_types** | [**Dict[str, EntityTypeVersionLoadConfig]**](EntityTypeVersionLoadConfig.md) |  | [optional] |
| **rollback_on_error** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.entity_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityTypeVersionLoadRequest.model_validate(data)` or `EntityTypeVersionLoadRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

