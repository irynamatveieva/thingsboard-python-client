
# EventFilter

`tb_paas_client.models.EventFilter`

Filter for various event types

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **event_type** | [**EventType**](EventType.md) | String value representing the event type | |
| **not_empty** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.event_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EventFilter.model_validate(data)` or `EventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

