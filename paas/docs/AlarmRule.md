
# AlarmRule

`tb_paas_client.models.AlarmRule`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **condition** | [**AlarmCondition**](AlarmCondition.md) | JSON object representing the alarm rule condition | [optional] |
| **alarm_details** | **str** | String value representing the additional details for an alarm rule | [optional] |
| **dashboard_id** | [**DashboardId**](DashboardId.md) | JSON object with the dashboard Id representing the reference to alarm details dashboard used by mobile application | [optional] |
| **schedule** | [**AlarmSchedule**](AlarmSchedule.md) | JSON object representing time interval during which the rule is active | [optional] |



## Referenced Types

> **EntityId types** (`DashboardId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

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
- **Attribute access:** `obj.condition`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRule.model_validate(data)` or `AlarmRule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

