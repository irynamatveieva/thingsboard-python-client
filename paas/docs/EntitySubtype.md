
# EntitySubtype

`tb_paas_client.models.EntitySubtype`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **entity_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **type** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.tenant_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntitySubtype.model_validate(data)` or `EntitySubtype.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

