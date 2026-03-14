
# TimeSeriesChartKeySettings

`tb_paas_client.models.TimeSeriesChartKeySettings`

**Extends:** **DataKeySettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **y_axis_id** | **str** |  | [optional] |
| **show_in_legend** | **bool** |  | [optional] |
| **series_type** | [**TimeSeriesChartSeriesType**](TimeSeriesChartSeriesType.md) |  | [optional] |
| **line_settings** | [**LineSeriesSettings**](LineSeriesSettings.md) |  | [optional] |
| **bar_settings** | [**BarSeriesSettings**](BarSeriesSettings.md) |  | [optional] |
| **comparison_settings** | [**DataKeyComparisonSettings**](DataKeyComparisonSettings.md) |  | [optional] |
| **yaxis_id** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.y_axis_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesChartKeySettings.model_validate(data)` or `TimeSeriesChartKeySettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

