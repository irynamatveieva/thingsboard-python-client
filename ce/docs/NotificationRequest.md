
# NotificationRequest

`tb_ce_client.models.NotificationRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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
| **id** | [**NotificationRequestId**](NotificationRequestId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.tenant_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRequest.model_validate(data)` or `NotificationRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

