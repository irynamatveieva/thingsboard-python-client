
# RelationsQueryFilter

`tb_paas_client.models.RelationsQueryFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **root_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |
| **multi_root** | **bool** |  | [optional] |
| **multi_root_entities_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **multi_root_entity_ids** | **List[str]** |  | [optional] |
| **direction** | [**EntitySearchDirection**](EntitySearchDirection.md) |  | [optional] |
| **filters** | [**List[RelationEntityTypeFilter]**](RelationEntityTypeFilter.md) |  | [optional] |
| **max_level** | **int** |  | [optional] |
| **fetch_last_level_only** | **bool** |  | [optional] |
| **negate** | **bool** |  | [optional] |
| **root_state_entity** | **bool** |  | [optional] |
| **default_state_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.root_entity`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelationsQueryFilter.model_validate(data)` or `RelationsQueryFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

