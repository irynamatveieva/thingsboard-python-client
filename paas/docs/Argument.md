
# Argument

`tb_paas_client.models.Argument`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **ref_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **ref_dynamic_source_configuration** | [**CfArgumentDynamicSourceConfiguration**](CfArgumentDynamicSourceConfiguration.md) |  | [optional] |
| **ref_entity_key** | [**ReferencedEntityKey**](ReferencedEntityKey.md) |  | [optional] |
| **default_value** | **str** |  | [optional] |
| **limit** | **int** |  | [optional] |
| **time_window** | **int** |  | [optional] |



## Referenced Types

> **EntityId**: `{entity_type: EntityType, id: UUID}` — base type for all entity identifiers.

#### CfArgumentDynamicSourceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### ReferencedEntityKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| type | ArgumentType |  | [optional] |
| scope | AttributeScope |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### ArgumentType (enum)
`TS_LATEST` | `ATTRIBUTE` | `TS_ROLLING`

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.ref_entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Argument.model_validate(data)` or `Argument.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

