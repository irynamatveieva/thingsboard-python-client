
# DeviceProfileAlarm

`tb_paas_client.models.DeviceProfileAlarm`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | String value representing the alarm rule id | [optional] |
| **alarm_type** | **str** | String value representing type of the alarm | [optional] |
| **create_rules** | [**Dict[str, AlarmRule]**](AlarmRule.md) | Complex JSON object representing create alarm rules. The unique create alarm rule can be created for each alarm severity type. There can be 5 create alarm rules configured per a single alarm type. See method implementation notes and AlarmRule model for more details | [optional] |
| **clear_rule** | [**AlarmRule**](AlarmRule.md) | JSON object representing clear alarm rule | [optional] |
| **propagate** | **bool** | Propagation flag to specify if alarm should be propagated to parent entities of alarm originator | [optional] |
| **propagate_to_owner** | **bool** | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator | [optional] |
| **propagate_to_owner_hierarchy** | **bool** | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) and all parent owners in the customer hierarchy | [optional] |
| **propagate_to_tenant** | **bool** | Propagation flag to specify if alarm should be propagated to the tenant entity | [optional] |
| **propagate_relation_types** | **List[str]** | JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored. | [optional] |



## Referenced Types

> **EntityId types** (`DashboardId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AlarmRule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| condition | AlarmCondition | JSON object representing the alarm rule condition | [optional] |
| alarm_details | str | String value representing the additional details for an alarm rule | [optional] |
| dashboard_id | DashboardId | JSON object with the dashboard Id representing the reference to alarm details dashboard used by mobile application | [optional] |
| schedule | AlarmSchedule | JSON object representing time interval during which the rule is active | [optional] |

#### AlarmCondition
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| condition | List[AlarmConditionFilter] |  | [optional] |
| spec | AlarmConditionSpec | JSON object representing alarm condition type | [optional] |

#### AlarmSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dynamic_value | DynamicValueString |  | [optional] |
| type | AlarmScheduleType |  | [optional] |

#### AlarmConditionFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value_type | EntityKeyValueType | String representation of the type of the value | [optional] |
| key | AlarmConditionFilterKey | JSON object for specifying alarm condition by specific key | [optional] |
| predicate | KeyFilterPredicate | JSON object representing filter condition | [optional] |
| value | object |  | [optional] |

#### AlarmConditionSpec
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DynamicValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | str |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### AlarmScheduleType (enum)
`ANY_TIME` | `SPECIFIC_TIME` | `CUSTOM`

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### AlarmConditionFilterKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AlarmConditionKeyType | The key type | [optional] |
| key | str | String value representing the key | [optional] |

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

#### AlarmConditionKeyType (enum)
`ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `CONSTANT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileAlarm.model_validate(data)` or `DeviceProfileAlarm.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

