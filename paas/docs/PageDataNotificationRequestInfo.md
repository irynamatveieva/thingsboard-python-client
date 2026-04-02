
# PageDataNotificationRequestInfo

`tb_paas_client.models.PageDataNotificationRequestInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[NotificationRequestInfo]**](NotificationRequestInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`DashboardId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTemplateId`, `ReportId`, `ReportTemplateId`, `TenantId`, `UserId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### NotificationRequestInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | NotificationRequestId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| targets | List[UUID] |  |  |
| template_id | NotificationTemplateId |  | [optional] |
| template | NotificationTemplate |  | [optional] |
| info | NotificationInfo |  | [optional] |
| additional_config | NotificationRequestConfig |  | [optional] |
| originator_entity_id | EntityId |  | [optional] |
| rule_id | NotificationRuleId |  | [optional] |
| status | NotificationRequestStatus |  | [optional] |
| stats | NotificationRequestStats |  | [optional] |
| template_name | str |  | [optional] |
| delivery_methods | List[NotificationDeliveryMethod] |  | [optional] |

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

#### NotificationDeliveryMethod (enum)
`WEB` | `EMAIL` | `SMS` | `SLACK` | `MICROSOFT_TEAMS` | `MOBILE_APP`

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
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataNotificationRequestInfo.model_validate(data)` or `PageDataNotificationRequestInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

