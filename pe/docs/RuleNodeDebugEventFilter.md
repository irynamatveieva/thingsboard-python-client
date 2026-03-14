
# RuleNodeDebugEventFilter

`tb_pe_client.models.RuleNodeDebugEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **is_error** | **Is_errorEnum** | Boolean value to filter the errors | [optional] |
| **error_str** | **str** | The case insensitive 'contains' filter based on error message | [optional] |
| **msg_direction_type** | **Msg_direction_typeEnum** | String value representing msg direction type (incoming to entity or outcoming from entity) | [optional] |
| **entity_id** | **str** | String value representing the entity id in the event body (originator of the message) | [optional] |
| **entity_type** | **Entity_typeEnum** | String value representing the entity type | [optional] |
| **msg_id** | **str** | String value representing the message id in the rule engine | [optional] |
| **msg_type** | **str** | String value representing the message type | [optional] |
| **relation_type** | **str** | String value representing the type of message routing | [optional] |
| **data_search** | **str** | The case insensitive 'contains' filter based on data (key and value) for the message. | [optional] |
| **metadata_search** | **str** | The case insensitive 'contains' filter based on metadata (key and value) for the message. | [optional] |


### Enum: Is_errorEnum

| Name | Value |
|---- | -----|
| &#39;false&#39; | 'false' |
| &#39;true&#39; | 'true' |


### Enum: Msg_direction_typeEnum

| Name | Value |
|---- | -----|
| &#39;IN&#39; | 'IN' |
| &#39;OUT&#39; | 'OUT' |


### Enum: Entity_typeEnum

| Name | Value |
|---- | -----|
| &#39;DEVICE&#39; | 'DEVICE' |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleNodeDebugEventFilter.model_validate(data)` or `RuleNodeDebugEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

