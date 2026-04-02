
# StatisticsEventFilter

`tb_pe_client.models.StatisticsEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **min_messages_processed** | **int** | The minimum number of successfully processed messages | [optional] |
| **max_messages_processed** | **int** | The maximum number of successfully processed messages | [optional] |
| **min_errors_occurred** | **int** | The minimum number of errors occurred during messages processing | [optional] |
| **max_errors_occurred** | **int** | The maximum number of errors occurred during messages processing | [optional] |



## Referenced Types

#### EventFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| event_type | EventType | String value representing the event type |  |
| not_empty | bool |  | [optional] |

#### CalculatedFieldDebugEventFilter  *(extends EventFilter, event_type=`DEBUG_CALCULATED_FIELD`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| is_error | Is_errorEnum | Boolean value to filter the errors | [optional] |
| error_str | str | The case insensitive 'contains' filter based on error message | [optional] |
| entity_id | str | String value representing the entity id in the event body | [optional] |
| entity_type | Entity_typeEnum | String value representing the entity type | [optional] |
| msg_id | str | String value representing the message id in the rule engine | [optional] |
| msg_type | str | String value representing the message type | [optional] |
| arguments | str | String value representing the arguments that were used in the calculation performed | [optional] |
| result | str | String value representing the result of a calculation | [optional] |

#### DebugConverterEventFilter  *(extends EventFilter, event_type=`DEBUG_CONVERTER`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| is_error | Is_errorEnum | Boolean value to filter the errors | [optional] |
| error_str | str | The case insensitive 'contains' filter based on error message | [optional] |
| type | str |  | [optional] |
| var_in | str |  | [optional] |
| out | str |  | [optional] |
| metadata | str |  | [optional] |

#### DebugIntegrationEventFilter  *(extends EventFilter, event_type=`DEBUG_INTEGRATION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| is_error | Is_errorEnum | Boolean value to filter the errors | [optional] |
| error_str | str | The case insensitive 'contains' filter based on error message | [optional] |
| type | str |  | [optional] |
| message | str |  | [optional] |
| status_integration | str |  | [optional] |

#### RuleChainDebugEventFilter  *(extends EventFilter, event_type=`DEBUG_RULE_CHAIN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| is_error | Is_errorEnum | Boolean value to filter the errors | [optional] |
| error_str | str | The case insensitive 'contains' filter based on error message | [optional] |
| message | str | String value representing the message | [optional] |

#### RuleNodeDebugEventFilter  *(extends EventFilter, event_type=`DEBUG_RULE_NODE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| is_error | Is_errorEnum | Boolean value to filter the errors | [optional] |
| error_str | str | The case insensitive 'contains' filter based on error message | [optional] |
| msg_direction_type | Msg_direction_typeEnum | String value representing msg direction type (incoming to entity or outcoming from entity) | [optional] |
| entity_id | str | String value representing the entity id in the event body (originator of the message) | [optional] |
| entity_type | Entity_typeEnum | String value representing the entity type | [optional] |
| msg_id | str | String value representing the message id in the rule engine | [optional] |
| msg_type | str | String value representing the message type | [optional] |
| relation_type | str | String value representing the type of message routing | [optional] |
| data_search | str | The case insensitive 'contains' filter based on data (key and value) for the message. | [optional] |
| metadata_search | str | The case insensitive 'contains' filter based on metadata (key and value) for the message. | [optional] |

#### ErrorEventFilter  *(extends EventFilter, event_type=`ERROR`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| method | str | String value representing the method name when the error happened | [optional] |
| error_str | str | The case insensitive 'contains' filter based on error message | [optional] |

#### LifeCycleEventFilter  *(extends EventFilter, event_type=`LC_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| event | str | String value representing the lifecycle event type | [optional] |
| status | StatusEnum | String value representing status of the lifecycle event | [optional] |
| error_str | str | The case insensitive 'contains' filter based on error message | [optional] |

#### RawDataEventFilter  *(extends EventFilter, event_type=`RAW_DATA`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| server | str | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| uuid | str | String value representing the uuid | [optional] |
| message_type | str | String value representing the message type | [optional] |
| message | str | String value representing the message | [optional] |

#### EventType (enum)
`ERROR` | `LC_EVENT` | `STATS` | `RAW_DATA` | `DEBUG_RULE_NODE` | `DEBUG_RULE_CHAIN` | `DEBUG_CONVERTER` | `DEBUG_INTEGRATION` | `DEBUG_CALCULATED_FIELD`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StatisticsEventFilter.model_validate(data)` or `StatisticsEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

