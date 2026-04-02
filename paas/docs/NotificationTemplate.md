
# NotificationTemplate

`tb_paas_client.models.NotificationTemplate`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **name** | **str** |  | |
| **notification_type** | [**NotificationType**](NotificationType.md) |  | |
| **configuration** | [**NotificationTemplateConfig**](NotificationTemplateConfig.md) |  | |



## Referenced Types

> **EntityId types** (`NotificationTemplateId`, `ReportTemplateId`, `TenantId`, `UserId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

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

#### DeliveryMethodNotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| body | str |  |  |
| method | str |  |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationTemplate.model_validate(data)` or `NotificationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

