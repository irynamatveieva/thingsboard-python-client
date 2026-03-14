
# SingleEntityVersionCreateRequest

`tb_paas_client.models.SingleEntityVersionCreateRequest`

**Extends:** **VersionCreateRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **config** | [**VersionCreateConfig**](VersionCreateConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SingleEntityVersionCreateRequest.model_validate(data)` or `SingleEntityVersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

