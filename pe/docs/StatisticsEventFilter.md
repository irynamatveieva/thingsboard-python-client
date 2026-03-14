
# StatisticsEventFilter

`tb_pe_client.models.StatisticsEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **min_messages_processed** | **int** | The minimum number of successfully processed messages | [optional] |
| **max_messages_processed** | **int** | The maximum number of successfully processed messages | [optional] |
| **min_errors_occurred** | **int** | The minimum number of errors occurred during messages processing | [optional] |
| **max_errors_occurred** | **int** | The maximum number of errors occurred during messages processing | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StatisticsEventFilter.model_validate(data)` or `StatisticsEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

