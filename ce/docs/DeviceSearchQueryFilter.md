
# DeviceSearchQueryFilter

`tb_ce_client.models.DeviceSearchQueryFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **root_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |
| **relation_type** | **str** |  | [optional] |
| **direction** | [**EntitySearchDirection**](EntitySearchDirection.md) |  | [optional] |
| **max_level** | **int** |  | [optional] |
| **fetch_last_level_only** | **bool** |  | [optional] |
| **root_state_entity** | **bool** |  | [optional] |
| **default_state_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |
| **device_types** | **List[str]** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.root_entity`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceSearchQueryFilter.model_validate(data)` or `DeviceSearchQueryFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

