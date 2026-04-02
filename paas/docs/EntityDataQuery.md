
# EntityDataQuery

`tb_paas_client.models.EntityDataQuery`

Entity data query to find entities. Page size is capped at 100.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_filter** | [**EntityFilter**](EntityFilter.md) |  | [optional] |
| **key_filters** | [**List[KeyFilter]**](KeyFilter.md) |  | [optional] |
| **page_link** | [**EntityDataPageLink**](EntityDataPageLink.md) |  | [optional] |
| **entity_fields** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **latest_values** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |



## Referenced Types

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

#### EntityDataPageLink
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| page_size | int |  | [optional] |
| page | int |  | [optional] |
| text_search | str |  | [optional] |
| sort_order | EntityDataSortOrder |  | [optional] |
| dynamic | bool |  | [optional] |

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

#### EntityKeyType (enum)
`ATTRIBUTE` | `CLIENT_ATTRIBUTE` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `ALARM_FIELD`

#### Direction (enum)
`ASC` | `DESC`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataQuery.model_validate(data)` or `EntityDataQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

