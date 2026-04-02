
# NotificationRequest

`tb_paas_client.models.NotificationRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**NotificationRequestId**](NotificationRequestId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **targets** | **List[UUID]** |  | |
| **template_id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | [optional] |
| **template** | [**NotificationTemplate**](NotificationTemplate.md) |  | [optional] |
| **info** | [**NotificationInfo**](NotificationInfo.md) |  | [optional] |
| **additional_config** | [**NotificationRequestConfig**](NotificationRequestConfig.md) |  | [optional] |
| **originator_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **rule_id** | [**NotificationRuleId**](NotificationRuleId.md) |  | [optional] |
| **status** | [**NotificationRequestStatus**](NotificationRequestStatus.md) |  | [optional] |
| **stats** | [**NotificationRequestStats**](NotificationRequestStats.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`DashboardId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTemplateId`, `ReportId`, `ReportTemplateId`, `TenantId`, `UserId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### NotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | NotificationTemplateId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| name | str |  |  |
| notification_type | NotificationType |  |  |
| configuration | NotificationTemplateConfig |  |  |

#### NotificationInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dashboard_id | DashboardId |  | [optional] |
| state_entity_id | EntityId |  | [optional] |
| type | str |  |  |

#### NotificationRequestConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sending_delay_in_sec | int |  | [optional] |
| reports | List[ReportId] |  | [optional] |

#### NotificationRequestStatus (enum)
`PROCESSING` | `SENT` | `SCHEDULED`

#### NotificationRequestStats
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sent | Dict[str, int] |  | [optional] |
| errors | Dict[str, Dict[str, str]] |  | [optional] |
| total_errors | int |  | [optional] |
| error | str |  | [optional] |
| total_sent | int |  | [optional] |

#### NotificationType (enum)
`GENERAL` | `ALARM` | `DEVICE_ACTIVITY` | `ENTITY_ACTION` | `ALARM_COMMENT` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `ALARM_ASSIGNMENT` | `NEW_PLATFORM_VERSION` | `ENTITIES_LIMIT` | `ENTITIES_LIMIT_INCREASE_REQUEST` | … (24 values total)

#### NotificationTemplateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| delivery_methods_templates | Dict[str, DeliveryMethodNotificationTemplate] |  |  |
| attach_report | bool |  | [optional] |
| report_template_id | ReportTemplateId |  | [optional] |
| user_id | UserId |  | [optional] |
| timezone | str |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### DeliveryMethodNotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| body | str |  |  |
| method | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRequest.model_validate(data)` or `NotificationRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

