
# StateEntityOwnerFilter

`tb_paas_client.models.StateEntityOwnerFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **single_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |
| **default_state_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.single_entity`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StateEntityOwnerFilter.model_validate(data)` or `StateEntityOwnerFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

