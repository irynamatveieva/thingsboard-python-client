
# SingleEntityVersionLoadRequest

`tb_paas_client.models.SingleEntityVersionLoadRequest`

**Extends:** **VersionLoadRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **internal_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **external_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **config** | [**VersionLoadConfig**](VersionLoadConfig.md) |  | [optional] |



## Referenced Types

> **EntityId**: `{entity_type: EntityType, id: UUID}` — base type for all entity identifiers.

#### VersionLoadRequest
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version_id | str |  | [optional] |
| type | VersionLoadRequestType | Type of the version to load |  |

#### VersionLoadConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| load_relations | bool |  | [optional] |
| load_attributes | bool |  | [optional] |
| load_credentials | bool |  | [optional] |
| load_calculated_fields | bool |  | [optional] |
| load_permissions | bool |  | [optional] |
| load_group_entities | bool |  | [optional] |
| auto_generate_integration_key | bool |  | [optional] |

#### VersionLoadRequestType (enum)
`SINGLE_ENTITY` | `ENTITY_TYPE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.internal_entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SingleEntityVersionLoadRequest.model_validate(data)` or `SingleEntityVersionLoadRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

