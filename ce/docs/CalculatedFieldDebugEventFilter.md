
# CalculatedFieldDebugEventFilter

`tb_ce_client.models.CalculatedFieldDebugEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **is_error** | **Is_errorEnum** | Boolean value to filter the errors | [optional] |
| **error_str** | **str** | The case insensitive 'contains' filter based on error message | [optional] |
| **entity_id** | **str** | String value representing the entity id in the event body | [optional] |
| **entity_type** | **Entity_typeEnum** | String value representing the entity type | [optional] |
| **msg_id** | **str** | String value representing the message id in the rule engine | [optional] |
| **msg_type** | **str** | String value representing the message type | [optional] |
| **arguments** | **str** | String value representing the arguments that were used in the calculation performed | [optional] |
| **result** | **str** | String value representing the result of a calculation | [optional] |


### Enum: Is_errorEnum

| Name | Value |
|---- | -----|
| &#39;false&#39; | 'false' |
| &#39;true&#39; | 'true' |


### Enum: Entity_typeEnum

| Name | Value |
|---- | -----|
| &#39;DEVICE&#39; | 'DEVICE' |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CalculatedFieldDebugEventFilter.model_validate(data)` or `CalculatedFieldDebugEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

