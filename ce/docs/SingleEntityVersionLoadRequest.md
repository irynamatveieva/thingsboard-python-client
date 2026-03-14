
# SingleEntityVersionLoadRequest

`tb_ce_client.models.SingleEntityVersionLoadRequest`

**Extends:** **VersionLoadRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **external_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **config** | [**VersionLoadConfig**](VersionLoadConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.external_entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SingleEntityVersionLoadRequest.model_validate(data)` or `SingleEntityVersionLoadRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

