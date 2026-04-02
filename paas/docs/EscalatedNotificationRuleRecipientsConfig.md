
# EscalatedNotificationRuleRecipientsConfig

`tb_paas_client.models.EscalatedNotificationRuleRecipientsConfig`

Escalated notification rule recipients configuration

**Extends:** **NotificationRuleRecipientsConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **escalation_table** | **Dict[str, List[UUID]]** |  | |



## Referenced Types

#### NotificationRuleRecipientsConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| trigger_type | NotificationRuleTriggerType |  | [optional] |

#### AlarmAssignmentRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ALARM_ASSIGNMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### AlarmCommentRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ALARM_COMMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### ApiUsageLimitRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`API_USAGE_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### DeviceActivityRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`DEVICE_ACTIVITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EdgeCommunicationFailureRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`EDGE_COMMUNICATION_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EdgeConnectionRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`EDGE_CONNECTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EntitiesLimitRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ENTITIES_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EntityActionRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ENTITY_ACTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### IntegrationLifecycleEventRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`INTEGRATION_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### NewPlatformVersionRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`NEW_PLATFORM_VERSION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### RateLimitsRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`RATE_LIMITS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### ResourceShortageRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`RESOURCES_SHORTAGE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### RuleEngineComponentLifecycleEventRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### TaskProcessingFailureRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`TASK_PROCESSING_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `INTEGRATION_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | … (15 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.escalation_table`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EscalatedNotificationRuleRecipientsConfig.model_validate(data)` or `EscalatedNotificationRuleRecipientsConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

