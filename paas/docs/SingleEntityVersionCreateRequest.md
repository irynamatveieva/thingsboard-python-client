
# SingleEntityVersionCreateRequest

`tb_paas_client.models.SingleEntityVersionCreateRequest`

**Extends:** **VersionCreateRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **config** | [**VersionCreateConfig**](VersionCreateConfig.md) |  | [optional] |



## Referenced Types

> **EntityId**: `{entity_type: EntityType, id: UUID}` — base type for all entity identifiers.

#### VersionCreateRequest
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version_name | str |  | [optional] |
| branch | str |  | [optional] |
| type | VersionCreateRequestType | Type of the version to create |  |

#### VersionCreateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| save_relations | bool |  | [optional] |
| save_attributes | bool |  | [optional] |
| save_credentials | bool |  | [optional] |
| save_calculated_fields | bool |  | [optional] |
| save_permissions | bool |  | [optional] |
| save_group_entities | bool |  | [optional] |

#### VersionCreateRequestType (enum)
`SINGLE_ENTITY` | `COMPLEX`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SingleEntityVersionCreateRequest.model_validate(data)` or `SingleEntityVersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

