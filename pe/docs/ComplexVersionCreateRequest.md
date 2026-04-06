
# ComplexVersionCreateRequest

`tb_pe_client.models.ComplexVersionCreateRequest`

**Extends:** **VersionCreateRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sync_strategy** | [**SyncStrategy**](SyncStrategy.md) |  | [optional] |
| **entity_types** | [**Dict[str, EntityTypeVersionCreateConfig]**](EntityTypeVersionCreateConfig.md) |  | [optional] |



## Referenced Types

#### VersionCreateRequest
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version_name | str |  | [optional] |
| branch | str |  | [optional] |
| type | VersionCreateRequestType | Type of the version to create |  |

#### SyncStrategy (enum)
`MERGE` | `OVERWRITE`

#### EntityTypeVersionCreateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| save_relations | bool |  | [optional] |
| save_attributes | bool |  | [optional] |
| save_credentials | bool |  | [optional] |
| save_calculated_fields | bool |  | [optional] |
| save_permissions | bool |  | [optional] |
| save_group_entities | bool |  | [optional] |
| sync_strategy | SyncStrategy |  | [optional] |
| entity_ids | List[UUID] |  | [optional] |
| all_entities | bool |  | [optional] |

#### VersionCreateRequestType (enum)
`SINGLE_ENTITY` | `COMPLEX`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.sync_strategy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ComplexVersionCreateRequest.model_validate(data)` or `ComplexVersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

