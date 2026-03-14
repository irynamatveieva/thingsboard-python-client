
# ComplexVersionCreateRequest

`tb_paas_client.models.ComplexVersionCreateRequest`

**Extends:** **VersionCreateRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sync_strategy** | [**SyncStrategy**](SyncStrategy.md) |  | [optional] |
| **entity_types** | [**Dict[str, EntityTypeVersionCreateConfig]**](EntityTypeVersionCreateConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.sync_strategy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ComplexVersionCreateRequest.model_validate(data)` or `ComplexVersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

