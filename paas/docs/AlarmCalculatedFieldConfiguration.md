
# AlarmCalculatedFieldConfiguration

`tb_paas_client.models.AlarmCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **clear_rule** | [**AlarmRuleDefinition**](AlarmRuleDefinition.md) |  | [optional] |
| **create_rules** | [**Dict[str, AlarmRuleDefinition]**](AlarmRuleDefinition.md) |  | |
| **propagate** | **bool** |  | [optional] |
| **propagate_relation_types** | **List[str]** |  | [optional] |
| **propagate_to_owner** | **bool** |  | [optional] |
| **propagate_to_owner_hierarchy** | **bool** |  | [optional] |
| **propagate_to_tenant** | **bool** |  | [optional] |



## Referenced Types

> **EntityId types** (`DashboardId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

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

#### AlarmRuleDefinition
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_details | str |  | [optional] |
| condition | AlarmRuleCondition |  |  |
| dashboard_id | DashboardId |  | [optional] |

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

#### AlarmRuleCondition
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| expression | AlarmConditionExpression |  |  |
| schedule | AlarmConditionValueAlarmRuleSchedule |  | [optional] |
| type | str |  |  |

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### ArgumentType (enum)
`TS_LATEST` | `ATTRIBUTE` | `TS_ROLLING`

#### AlarmConditionExpression
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmConditionValueAlarmRuleSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dynamic_value_argument | str |  | [optional] |
| static_value | AlarmRuleSchedule |  | [optional] |

#### AlarmRuleSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmCalculatedFieldConfiguration.model_validate(data)` or `AlarmCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

