
# DebugConverterEventFilter

`tb_pe_client.models.DebugConverterEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **is_error** | **Is_errorEnum** | Boolean value to filter the errors | [optional] |
| **error_str** | **str** | The case insensitive 'contains' filter based on error message | [optional] |
| **type** | **str** |  | [optional] |
| **var_in** | **str** |  | [optional] |
| **out** | **str** |  | [optional] |
| **metadata** | **str** |  | [optional] |


### Enum: Is_errorEnum

| Name | Value |
|---- | -----|
| &#39;false&#39; | 'false' |
| &#39;true&#39; | 'true' |



## Referenced Types

#### EventFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| event_type | EventType | String value representing the event type |  |
| not_empty | bool |  | [optional] |

#### EventType (enum)
`ERROR` | `LC_EVENT` | `STATS` | `RAW_DATA` | `DEBUG_RULE_NODE` | `DEBUG_RULE_CHAIN` | `DEBUG_CONVERTER` | `DEBUG_INTEGRATION` | `DEBUG_CALCULATED_FIELD`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DebugConverterEventFilter.model_validate(data)` or `DebugConverterEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

