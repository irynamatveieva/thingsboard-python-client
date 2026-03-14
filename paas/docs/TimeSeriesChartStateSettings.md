
# TimeSeriesChartStateSettings

`tb_paas_client.models.TimeSeriesChartStateSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **label** | **str** |  | [optional] |
| **value** | **float** |  | [optional] |
| **source_type** | [**TimeSeriesChartStateSourceType**](TimeSeriesChartStateSourceType.md) |  | [optional] |
| **source_range_from** | **float** |  | [optional] |
| **source_range_to** | **float** |  | [optional] |
| **source_value** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.label`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesChartStateSettings.model_validate(data)` or `TimeSeriesChartStateSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

