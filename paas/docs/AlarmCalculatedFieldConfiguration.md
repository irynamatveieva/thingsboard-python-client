
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

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

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

#### AttributesOutput  *(extends Output, type=`ATTRIBUTES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | AttributesOutputStrategy |  | [optional] |

#### TimeSeriesOutput  *(extends Output, type=`TIME_SERIES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | TimeSeriesOutputStrategy |  | [optional] |

#### CfArgumentDynamicSourceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CurrentOwnerDynamicSourceConfiguration  *(extends CfArgumentDynamicSourceConfiguration, type=`CURRENT_OWNER`)*
*See CfArgumentDynamicSourceConfiguration for properties.*

#### RelationPathQueryDynamicSourceConfiguration  *(extends CfArgumentDynamicSourceConfiguration, type=`RELATION_PATH_QUERY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| levels | List[RelationPathLevel] |  | [optional] |

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

#### AlarmRuleDurationCondition  *(extends AlarmRuleCondition, type=`DURATION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| unit | TimeUnit |  |  |
| value | AlarmConditionValueLong |  |  |

#### AlarmRuleRepeatingCondition  *(extends AlarmRuleCondition, type=`REPEATING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| count | AlarmConditionValueInteger |  |  |

#### AlarmRuleSimpleCondition  *(extends AlarmRuleCondition, type=`SIMPLE`)*
*See AlarmRuleCondition for properties.*

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

#### SimpleAlarmConditionExpression  *(extends AlarmConditionExpression, type=`SIMPLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| filters | List[AlarmRuleConditionFilter] |  |  |
| operation | ComplexOperation |  | [optional] |

#### TbelAlarmConditionExpression  *(extends AlarmConditionExpression, type=`TBEL`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| expression | str |  |  |

#### AlarmConditionValueAlarmRuleSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dynamic_value_argument | str |  | [optional] |
| static_value | AlarmRuleSchedule |  | [optional] |

#### TimeSeriesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TimeSeriesImmediateOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ttl | int |  | [optional] |
| save_time_series | bool |  | [optional] |
| save_latest | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### TimeSeriesRuleChainOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`RULE_CHAIN`)*
*See TimeSeriesOutputStrategy for properties.*

#### AttributesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AttributesImmediateOutputStrategy  *(extends AttributesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| send_attributes_updated_notification | bool |  | [optional] |
| update_attributes_only_on_value_change | bool |  | [optional] |
| save_attribute | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### AttributesRuleChainOutputStrategy  *(extends AttributesOutputStrategy, type=`RULE_CHAIN`)*
*See AttributesOutputStrategy for properties.*

#### RelationPathLevel
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| direction | EntitySearchDirection |  |  |
| relation_type | str |  |  |

#### AlarmRuleSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmRuleAnyTimeSchedule  *(extends AlarmRuleSchedule, type=`ANY_TIME`)*
*See AlarmRuleSchedule for properties.*

#### AlarmRuleCustomTimeSchedule  *(extends AlarmRuleSchedule, type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| items | List[AlarmRuleCustomTimeScheduleItem] |  | [optional] |
| timezone | str |  | [optional] |

#### AlarmRuleSpecificTimeSchedule  *(extends AlarmRuleSchedule, type=`SPECIFIC_TIME`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| days_of_week | List[int] |  | [optional] |
| ends_on | int |  | [optional] |
| starts_on | int |  | [optional] |
| timezone | str |  | [optional] |

#### TimeUnit (enum)
`NANOSECONDS` | `MICROSECONDS` | `MILLISECONDS` | `SECONDS` | `MINUTES` | `HOURS` | `DAYS`

#### AlarmConditionValueLong
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | int |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmConditionValueInteger
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | int |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### AlarmRuleConditionFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| argument | str |  |  |
| operation | ComplexOperation |  | [optional] |
| predicates | List[AlarmRuleKeyFilterPredicate] |  |  |
| value_type | EntityKeyValueType |  |  |

#### ComplexOperation (enum)
`AND` | `OR`

#### AlarmRuleKeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmRuleBooleanFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`BOOLEAN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | BooleanOperation |  |  |
| value | AlarmConditionValueBoolean |  |  |

#### AlarmRuleComplexFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | ComplexOperation |  | [optional] |
| predicates | List[AlarmRuleKeyFilterPredicate] |  | [optional] |

#### AlarmRuleNoDataFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`NO_DATA`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| duration | AlarmConditionValueLong |  |  |
| unit | TimeUnit |  |  |

#### AlarmRuleNumericFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`NUMERIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | NumericOperation |  |  |
| value | AlarmConditionValueDouble |  |  |

#### AlarmRuleStringFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`STRING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ignore_case | bool |  | [optional] |
| operation | StringOperation |  |  |
| value | AlarmConditionValueString |  |  |

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### AlarmRuleCustomTimeScheduleItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| day_of_week | int |  | [optional] |
| enabled | bool |  | [optional] |
| ends_on | int |  | [optional] |
| starts_on | int |  | [optional] |

#### StringOperation (enum)
`EQUAL` | `NOT_EQUAL` | `STARTS_WITH` | `ENDS_WITH` | `CONTAINS` | `NOT_CONTAINS` | `IN` | `NOT_IN`

#### AlarmConditionValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | str |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### NumericOperation (enum)
`EQUAL` | `NOT_EQUAL` | `GREATER` | `LESS` | `GREATER_OR_EQUAL` | `LESS_OR_EQUAL`

#### AlarmConditionValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | float |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### BooleanOperation (enum)
`EQUAL` | `NOT_EQUAL`

#### AlarmConditionValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | bool |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmCalculatedFieldConfiguration.model_validate(data)` or `AlarmCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

