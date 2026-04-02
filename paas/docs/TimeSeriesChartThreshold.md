
# TimeSeriesChartThreshold

`tb_paas_client.models.TimeSeriesChartThreshold`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**ValueSourceType**](ValueSourceType.md) |  | [optional] |
| **value** | **float** |  | [optional] |
| **latest_key_type** | **str** |  | [optional] |
| **latest_key** | **str** |  | [optional] |
| **entity_key_type** | **str** |  | [optional] |
| **entity_alias** | **str** |  | [optional] |
| **entity_key** | **str** |  | [optional] |
| **y_axis_id** | **str** |  | [optional] |
| **units** | **str** |  | [optional] |
| **decimals** | **int** |  | [optional] |
| **line_color** | **str** |  | [optional] |
| **line_type** | [**ChartLineType**](ChartLineType.md) |  | [optional] |
| **line_width** | **float** |  | [optional] |
| **start_symbol** | [**ChartShape**](ChartShape.md) |  | [optional] |
| **start_symbol_size** | **float** |  | [optional] |
| **end_symbol** | [**ChartShape**](ChartShape.md) |  | [optional] |
| **end_symbol_size** | **float** |  | [optional] |
| **show_label** | **bool** |  | [optional] |
| **label_position** | [**ThresholdLabelPosition**](ThresholdLabelPosition.md) |  | [optional] |
| **label_font** | [**Font**](Font.md) |  | [optional] |
| **label_color** | **str** |  | [optional] |
| **enable_label_background** | **bool** |  | [optional] |
| **label_background** | **str** |  | [optional] |
| **yaxis_id** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesChartThreshold.model_validate(data)` or `TimeSeriesChartThreshold.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

