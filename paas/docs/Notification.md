
# Notification

`tb_paas_client.models.Notification`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **request_id** | [**NotificationRequestId**](NotificationRequestId.md) |  | [optional] |
| **recipient_id** | [**UserId**](UserId.md) |  | [optional] |
| **type** | [**NotificationType**](NotificationType.md) |  | [optional] |
| **delivery_method** | [**NotificationDeliveryMethod**](NotificationDeliveryMethod.md) |  | [optional] |
| **subject** | **str** |  | [optional] |
| **text** | **str** |  | [optional] |
| **additional_config** | **object** |  | [optional] |
| **info** | [**NotificationInfo**](NotificationInfo.md) |  | [optional] |
| **status** | [**NotificationStatus**](NotificationStatus.md) |  | [optional] |
| **id** | [**NotificationId**](NotificationId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.request_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Notification.model_validate(data)` or `Notification.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

