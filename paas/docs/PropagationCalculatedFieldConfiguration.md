
# PropagationCalculatedFieldConfiguration

`tb_paas_client.models.PropagationCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **apply_expression_to_resolved_arguments** | **bool** |  | [optional] |
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **expression** | **str** |  | [optional] |
| **relation** | [**RelationPathLevel**](RelationPathLevel.md) |  | |



## Referenced Types

> **EntityId**: `{entity_type: EntityType, id: UUID}` — base type for all entity identifiers.

#### CalculatedFieldConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |
| output | Output |  | [optional] |
| ai_generated | bool |  | [optional] |

#### Argument
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ref_entity_id | EntityId |  | [optional] |
| ref_dynamic_source_configuration | CfArgumentDynamicSourceConfiguration |  | [optional] |
| ref_entity_key | ReferencedEntityKey |  | [optional] |
| default_value | str |  | [optional] |
| limit | int |  | [optional] |
| time_window | int |  | [optional] |

#### RelationPathLevel
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| direction | EntitySearchDirection |  |  |
| relation_type | str |  |  |

#### Output
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str |  | [optional] |
| scope | AttributeScope |  | [optional] |
| decimals_by_default | int |  | [optional] |
| strategy | object |  | [optional] |
| type | str |  |  |

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

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### ArgumentType (enum)
`TS_LATEST` | `ATTRIBUTE` | `TS_ROLLING`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.apply_expression_to_resolved_arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PropagationCalculatedFieldConfiguration.model_validate(data)` or `PropagationCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

