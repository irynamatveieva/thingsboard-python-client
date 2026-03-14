
# AuditLog

`tb_pe_client.models.AuditLog`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AuditLogId**](AuditLogId.md) | JSON object with the auditLog Id | [optional] |
| **created_time** | **int** | Timestamp of the auditLog creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id | [optional] [readonly] |
| **entity_id** | [**EntityId**](EntityId.md) | JSON object with Entity id | [optional] [readonly] |
| **entity_name** | **str** | Name of the logged entity | [optional] [readonly] |
| **user_id** | [**UserId**](UserId.md) | JSON object with User id. | [optional] [readonly] |
| **user_name** | **str** | Unique user name(email) of the user that performed some action on logged entity | [optional] [readonly] |
| **action_type** | [**ActionType**](ActionType.md) | String represented Action type | [optional] [readonly] |
| **action_data** | **object** | JsonNode represented action data | [optional] [readonly] |
| **action_status** | [**ActionStatus**](ActionStatus.md) | String represented Action status | [optional] [readonly] |
| **action_failure_details** | **str** | Failure action details info. An empty string in case of action status type 'SUCCESS', otherwise includes stack trace of the caused exception. | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AuditLog.model_validate(data)` or `AuditLog.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

