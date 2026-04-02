
# NotificationRuleRecipientsConfig

`tb_paas_client.models.NotificationRuleRecipientsConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **trigger_type** | [**NotificationRuleTriggerType**](NotificationRuleTriggerType.md) |  | [optional] |



## Subtypes

#### EscalatedNotificationRuleRecipientsConfig  *(trigger_type=`ALARM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| escalation_table | Dict[str, List[UUID]] |  |  |

#### AlarmAssignmentRecipientsConfig  *(trigger_type=`ALARM_ASSIGNMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### AlarmCommentRecipientsConfig  *(trigger_type=`ALARM_COMMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### ApiUsageLimitRecipientsConfig  *(trigger_type=`API_USAGE_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### DeviceActivityRecipientsConfig  *(trigger_type=`DEVICE_ACTIVITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EdgeCommunicationFailureRecipientsConfig  *(trigger_type=`EDGE_COMMUNICATION_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EdgeConnectionRecipientsConfig  *(trigger_type=`EDGE_CONNECTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EntitiesLimitRecipientsConfig  *(trigger_type=`ENTITIES_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EntityActionRecipientsConfig  *(trigger_type=`ENTITY_ACTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### IntegrationLifecycleEventRecipientsConfig  *(trigger_type=`INTEGRATION_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### NewPlatformVersionRecipientsConfig  *(trigger_type=`NEW_PLATFORM_VERSION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### RateLimitsRecipientsConfig  *(trigger_type=`RATE_LIMITS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### ResourceShortageRecipientsConfig  *(trigger_type=`RESOURCES_SHORTAGE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### RuleEngineComponentLifecycleEventRecipientsConfig  *(trigger_type=`RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### TaskProcessingFailureRecipientsConfig  *(trigger_type=`TASK_PROCESSING_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

## Referenced Types

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `INTEGRATION_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | … (15 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.trigger_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRuleRecipientsConfig.model_validate(data)` or `NotificationRuleRecipientsConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

