
# EntitiesByGroupNameFilter

`tb_pe_client.models.EntitiesByGroupNameFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **group_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **entity_group_name_filter** | **str** |  | [optional] |
| **group_state_entity** | **bool** |  | [optional] |
| **state_entity_param_name** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.group_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntitiesByGroupNameFilter.model_validate(data)` or `EntitiesByGroupNameFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

