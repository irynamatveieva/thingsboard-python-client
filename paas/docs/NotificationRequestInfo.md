
# NotificationRequestInfo

`tb_paas_client.models.NotificationRequestInfo`

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
| **template_name** | **str** |  | [optional] |
| **delivery_methods** | [**List[NotificationDeliveryMethod]**](NotificationDeliveryMethod.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRequestInfo.model_validate(data)` or `NotificationRequestInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

