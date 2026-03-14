
# NotificationRequestStats

`tb_ce_client.models.NotificationRequestStats`

Notification request processing statistics

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sent** | **Dict[str, int]** | Number of successfully sent notifications per delivery method | [optional] |
| **errors** | **Dict[str, Dict[str, str]]** | Errors per delivery method. Each entry maps recipient name to error message | [optional] |
| **total_errors** | **int** | Total number of errors across all delivery methods | [optional] |
| **error** | **str** | General error message if the entire request failed | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.sent`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRequestStats.model_validate(data)` or `NotificationRequestStats.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

