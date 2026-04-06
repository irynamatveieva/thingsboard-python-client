
# LifeCycleEventFilter

`tb_ce_client.models.LifeCycleEventFilter`

**Extends:** **EventFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **server** | **str** | String value representing the server name, identifier or ip address where the platform is running | [optional] |
| **event** | **str** | String value representing the lifecycle event type | [optional] |
| **status** | **StatusEnum** | String value representing status of the lifecycle event | [optional] |
| **error_str** | **str** | The case insensitive 'contains' filter based on error message | [optional] |


### Enum: StatusEnum

| Name | Value |
|---- | -----|
| &#39;Success&#39; | 'Success' |
| &#39;Failure&#39; | 'Failure' |



## Referenced Types

#### EventFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| event_type | EventType | String value representing the event type |  |
| not_empty | bool |  | [optional] |

#### EventType (enum)
`ERROR` | `LC_EVENT` | `STATS` | `DEBUG_RULE_NODE` | `DEBUG_RULE_CHAIN` | `DEBUG_CALCULATED_FIELD`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.server`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LifeCycleEventFilter.model_validate(data)` or `LifeCycleEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

