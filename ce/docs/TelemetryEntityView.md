
# TelemetryEntityView

`tb_ce_client.models.TelemetryEntityView`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timeseries** | **List[str]** | List of time-series data keys to expose | |
| **attributes** | [**AttributesEntityView**](AttributesEntityView.md) | JSON object with attributes to expose | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.timeseries`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TelemetryEntityView.model_validate(data)` or `TelemetryEntityView.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

