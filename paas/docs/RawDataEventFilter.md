
# RawDataEventFilter

`tb_paas_client.models.RawDataEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **uuid** | **str** | String value representing the uuid | [optional] |
| **message_type** | **str** | String value representing the message type | [optional] |
| **message** | **str** | String value representing the message | [optional] |



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

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RawDataEventFilter.model_validate(data)` or `RawDataEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

