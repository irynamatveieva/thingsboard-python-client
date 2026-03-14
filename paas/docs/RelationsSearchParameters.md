
# RelationsSearchParameters

`tb_paas_client.models.RelationsSearchParameters`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **root_id** | **UUID** | Root entity id to start search from. | [optional] |
| **root_type** | [**EntityType**](EntityType.md) | Type of the root entity. | [optional] |
| **direction** | [**EntitySearchDirection**](EntitySearchDirection.md) | Type of the root entity. | [optional] |
| **relation_type_group** | [**RelationTypeGroup**](RelationTypeGroup.md) | Type of the relation. | [optional] |
| **max_level** | **int** | Maximum level of the search depth. | [optional] |
| **fetch_last_level_only** | **bool** | Fetch entities that match the last level of search. Useful to find Devices that are strictly 'maxLevel' relations away from the root entity. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.root_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelationsSearchParameters.model_validate(data)` or `RelationsSearchParameters.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

