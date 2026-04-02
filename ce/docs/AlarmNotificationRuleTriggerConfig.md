
# AlarmNotificationRuleTriggerConfig

`tb_ce_client.models.AlarmNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **alarm_types** | **List[str]** |  | [optional] |
| **alarm_severities** | [**List[AlarmSeverity]**](AlarmSeverity.md) |  | [optional] |
| **notify_on** | [**List[AlarmAction]**](AlarmAction.md) |  | |
| **clear_rule** | [**ClearRule**](ClearRule.md) |  | [optional] |



## Referenced Types

#### NotificationRuleTriggerConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| trigger_type | NotificationRuleTriggerType |  |  |

#### AlarmAssignmentNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ALARM_ASSIGNMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |
| notify_on | List[Action] |  |  |

#### AlarmCommentNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ALARM_COMMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |
| only_user_comments | bool |  | [optional] |
| notify_on_comment_update | bool |  | [optional] |

#### ApiUsageLimitNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`API_USAGE_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_features | List[ApiFeature] |  | [optional] |
| notify_on | List[ApiUsageStateValue] |  | [optional] |

#### DeviceActivityNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`DEVICE_ACTIVITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| devices | List[UUID] |  | [optional] |
| device_profiles | List[UUID] |  | [optional] |
| notify_on | List[DeviceEvent] |  |  |

#### EdgeCommunicationFailureNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`EDGE_COMMUNICATION_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edges | List[UUID] |  | [optional] |

#### EdgeConnectionNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`EDGE_CONNECTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edges | List[UUID] |  | [optional] |
| notify_on | List[EdgeConnectivityEvent] |  | [optional] |

#### EntitiesLimitNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ENTITIES_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_types | List[EntityType] |  | [optional] |
| threshold | float |  | [optional] |

#### EntityActionNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ENTITY_ACTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_types | List[EntityType] |  | [optional] |
| created | bool |  | [optional] |
| updated | bool |  | [optional] |
| deleted | bool |  | [optional] |

#### NewPlatformVersionNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`NEW_PLATFORM_VERSION`)*
*See NotificationRuleTriggerConfig for properties.*

#### RateLimitsNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`RATE_LIMITS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| apis | List[LimitedApi] |  | [optional] |

#### ResourcesShortageNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`RESOURCES_SHORTAGE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| cpu_threshold | float |  | [optional] |
| ram_threshold | float |  | [optional] |
| storage_threshold | float |  | [optional] |

#### RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| rule_chains | List[UUID] |  | [optional] |
| rule_chain_events | List[ComponentLifecycleEvent] |  | [optional] |
| only_rule_chain_lifecycle_failures | bool |  | [optional] |
| track_rule_node_events | bool |  | [optional] |
| rule_node_events | List[ComponentLifecycleEvent] |  | [optional] |
| only_rule_node_lifecycle_failures | bool |  | [optional] |

#### TaskProcessingFailureNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`TASK_PROCESSING_FAILURE`)*
*See NotificationRuleTriggerConfig for properties.*

#### AlarmSeverity (enum)
`CRITICAL` | `MAJOR` | `MINOR` | `WARNING` | `INDETERMINATE`

#### AlarmAction (enum)
`CREATED` | `SEVERITY_CHANGED` | `ACKNOWLEDGED` | `CLEARED`

#### ClearRule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | `ENTITIES_LIMIT` | … (14 values total)

#### AlarmSearchStatus (enum)
`ANY` | `ACTIVE` | `CLEARED` | `ACK` | `UNACK`

#### DeviceEvent (enum)
`ACTIVE` | `INACTIVE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `RULE_CHAIN` | `RULE_NODE` | `ENTITY_VIEW` | … (36 values total)

#### ComponentLifecycleEvent (enum)
`CREATED` | `STARTED` | `ACTIVATED` | `SUSPENDED` | `UPDATED` | `STOPPED` | `DELETED` | `FAILED` | `DEACTIVATED` | `RELATION_UPDATED` | … (11 values total)

#### Action (enum)
`ASSIGNED` | `UNASSIGNED`

#### ApiFeature (enum)
`TRANSPORT` | `DB` | `RE` | `JS` | `TBEL` | `EMAIL` | `SMS` | `ALARM`

#### ApiUsageStateValue (enum)
`ENABLED` | `WARNING` | `DISABLED`

#### LimitedApi (enum)
`ENTITY_EXPORT` | `ENTITY_IMPORT` | `NOTIFICATION_REQUESTS` | `NOTIFICATION_REQUESTS_PER_RULE` | `REST_REQUESTS_PER_TENANT` | `REST_REQUESTS_PER_CUSTOMER` | `WS_UPDATES_PER_SESSION` | `CASSANDRA_WRITE_QUERIES_CORE` | `CASSANDRA_READ_QUERIES_CORE` | `CASSANDRA_WRITE_QUERIES_RULE_ENGINE` | … (28 values total)

#### EdgeConnectivityEvent (enum)
`CONNECTED` | `DISCONNECTED`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.alarm_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmNotificationRuleTriggerConfig.model_validate(data)` or `AlarmNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

