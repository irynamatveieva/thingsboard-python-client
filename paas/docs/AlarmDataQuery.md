
# AlarmDataQuery

`tb_paas_client.models.AlarmDataQuery`

A JSON value representing the alarm data query. See API call notes above for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_filter** | [**EntityFilter**](EntityFilter.md) |  | [optional] |
| **key_filters** | [**List[KeyFilter]**](KeyFilter.md) |  | [optional] |
| **page_link** | [**AlarmDataPageLink**](AlarmDataPageLink.md) |  | [optional] |
| **entity_fields** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **latest_values** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **alarm_fields** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`UserId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### KeyFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | EntityKey |  | [optional] |
| value_type | EntityKeyValueType |  | [optional] |
| predicate | KeyFilterPredicate |  | [optional] |

#### AlarmDataPageLink
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| page_size | int |  | [optional] |
| page | int |  | [optional] |
| text_search | str |  | [optional] |
| sort_order | EntityDataSortOrder |  | [optional] |
| dynamic | bool |  | [optional] |
| start_ts | int |  | [optional] |
| end_ts | int |  | [optional] |
| time_window | int |  | [optional] |
| type_list | List[str] |  | [optional] |
| status_list | List[AlarmSearchStatus] |  | [optional] |
| severity_list | List[AlarmSeverity] |  | [optional] |
| search_propagated_alarms | bool |  | [optional] |
| assignee_id | UserId |  | [optional] |

#### EntityKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | EntityKeyType |  | [optional] |
| key | str |  | [optional] |

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### EntityDataSortOrder
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | EntityKey |  | [optional] |
| direction | Direction |  | [optional] |

#### AlarmSearchStatus (enum)
`ANY` | `ACTIVE` | `CLEARED` | `ACK` | `UNACK`

#### AlarmSeverity (enum)
`CRITICAL` | `MAJOR` | `MINOR` | `WARNING` | `INDETERMINATE`

#### EntityKeyType (enum)
`ATTRIBUTE` | `CLIENT_ATTRIBUTE` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `ALARM_FIELD`

#### Direction (enum)
`ASC` | `DESC`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmDataQuery.model_validate(data)` or `AlarmDataQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

