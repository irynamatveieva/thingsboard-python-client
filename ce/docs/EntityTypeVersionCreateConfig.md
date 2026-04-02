
# EntityTypeVersionCreateConfig

`tb_ce_client.models.EntityTypeVersionCreateConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **save_relations** | **bool** |  | [optional] |
| **save_attributes** | **bool** |  | [optional] |
| **save_credentials** | **bool** |  | [optional] |
| **save_calculated_fields** | **bool** |  | [optional] |
| **sync_strategy** | [**SyncStrategy**](SyncStrategy.md) |  | [optional] |
| **entity_ids** | **List[UUID]** |  | [optional] |
| **all_entities** | **bool** |  | [optional] |



## Referenced Types

#### SyncStrategy (enum)
`MERGE` | `OVERWRITE`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.save_relations`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityTypeVersionCreateConfig.model_validate(data)` or `EntityTypeVersionCreateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

