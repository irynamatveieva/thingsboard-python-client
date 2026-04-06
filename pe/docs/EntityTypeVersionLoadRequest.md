
# EntityTypeVersionLoadRequest

`tb_pe_client.models.EntityTypeVersionLoadRequest`

**Extends:** **VersionLoadRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_types** | [**Dict[str, EntityTypeVersionLoadConfig]**](EntityTypeVersionLoadConfig.md) |  | [optional] |
| **rollback_on_error** | **bool** |  | [optional] |



## Referenced Types

#### VersionLoadRequest
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version_id | str |  | [optional] |
| type | VersionLoadRequestType | Type of the version to load |  |

#### EntityTypeVersionLoadConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| load_relations | bool |  | [optional] |
| load_attributes | bool |  | [optional] |
| load_credentials | bool |  | [optional] |
| load_calculated_fields | bool |  | [optional] |
| load_permissions | bool |  | [optional] |
| load_group_entities | bool |  | [optional] |
| auto_generate_integration_key | bool |  | [optional] |
| remove_other_entities | bool |  | [optional] |
| find_existing_entity_by_name | bool |  | [optional] |

#### VersionLoadRequestType (enum)
`SINGLE_ENTITY` | `ENTITY_TYPE`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityTypeVersionLoadRequest.model_validate(data)` or `EntityTypeVersionLoadRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

