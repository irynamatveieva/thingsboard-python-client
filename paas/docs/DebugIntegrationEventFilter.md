
# DebugIntegrationEventFilter

`tb_paas_client.models.DebugIntegrationEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **is_error** | **Is_errorEnum** | Boolean value to filter the errors | [optional] |
| **error_str** | **str** | The case insensitive 'contains' filter based on error message | [optional] |
| **type** | **str** |  | [optional] |
| **message** | **str** |  | [optional] |
| **status_integration** | **str** |  | [optional] |


### Enum: Is_errorEnum

| Name | Value |
|---- | -----|
| &#39;false&#39; | 'false' |
| &#39;true&#39; | 'true' |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DebugIntegrationEventFilter.model_validate(data)` or `DebugIntegrationEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

