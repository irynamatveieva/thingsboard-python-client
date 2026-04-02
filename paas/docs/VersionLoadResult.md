
# VersionLoadResult

`tb_paas_client.models.VersionLoadResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **result** | [**List[EntityTypeLoadResult]**](EntityTypeLoadResult.md) |  | [optional] |
| **error** | [**EntityLoadError**](EntityLoadError.md) |  | [optional] |
| **done** | **bool** |  | [optional] |



## Referenced Types

> **EntityId**: `{entity_type: EntityType, id: UUID}` — base type for all entity identifiers.

#### EntityTypeLoadResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| created | int |  | [optional] |
| updated | int |  | [optional] |
| deleted | int |  | [optional] |
| groups_created | int |  | [optional] |
| groups_updated | int |  | [optional] |
| groups_deleted | int |  | [optional] |

#### EntityLoadError
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  | [optional] |
| source | EntityId |  | [optional] |
| target | EntityId |  | [optional] |
| message | str |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.result`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionLoadResult.model_validate(data)` or `VersionLoadResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

