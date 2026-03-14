
# NotificationRequestStats

`tb_paas_client.models.NotificationRequestStats`

Notification request processing statistics

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sent** | **Dict[str, int]** |  | [optional] |
| **errors** | **Dict[str, Dict[str, str]]** |  | [optional] |
| **total_errors** | **int** |  | [optional] |
| **error** | **str** |  | [optional] |
| **total_sent** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.sent`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRequestStats.model_validate(data)` or `NotificationRequestStats.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

