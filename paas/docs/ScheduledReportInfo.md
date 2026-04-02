
# ScheduledReportInfo

`tb_paas_client.models.ScheduledReportInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**SchedulerEventId**](SchedulerEventId.md) | JSON object with the scheduler event Id. Specify this field to update the scheduler event. Referencing non-existing scheduler event Id will cause error. Omit this field to create new scheduler event | [optional] |
| **created_time** | **int** | Timestamp of the scheduler event creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the scheduler event | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id | [optional] [readonly] |
| **originator_id** | [**EntityId**](EntityId.md) | JSON object with Originator Id | [optional] [readonly] |
| **name** | **str** | scheduler event name | [optional] |
| **type** | **str** | scheduler event type | [optional] |
| **schedule** | **object** | a JSON value with schedule time configuration | [optional] |
| **enabled** | **bool** | Enable/disable scheduler | [optional] |
| **version** | **int** |  | [optional] |
| **template_info** | [**EntityInfo**](EntityInfo.md) | Report template info | [optional] [readonly] |
| **customer_title** | **str** | Customer title | [optional] [readonly] |
| **user_name** | **str** | Report user name | [optional] [readonly] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`CustomerId`, `SchedulerEventId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ScheduledReportInfo.model_validate(data)` or `ScheduledReportInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

