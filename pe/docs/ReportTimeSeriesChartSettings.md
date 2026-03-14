
# ReportTimeSeriesChartSettings

`tb_pe_client.models.ReportTimeSeriesChartSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_title** | **bool** |  | [optional] |
| **title** | **str** |  | [optional] |
| **title_font** | [**Font**](Font.md) |  | [optional] |
| **title_color** | **str** |  | [optional] |
| **title_alignment** | [**TextAlignment**](TextAlignment.md) |  | [optional] |
| **stack** | **bool** |  | [optional] |
| **comparison_enabled** | **bool** |  | [optional] |
| **time_for_comparison** | [**ComparisonDuration**](ComparisonDuration.md) |  | [optional] |
| **comparison_custom_interval_value** | **int** |  | [optional] |
| **show_legend** | **bool** |  | [optional] |
| **legend_column_title_font** | [**Font**](Font.md) |  | [optional] |
| **legend_column_title_color** | **str** |  | [optional] |
| **legend_label_font** | [**Font**](Font.md) |  | [optional] |
| **legend_label_color** | **str** |  | [optional] |
| **legend_value_font** | [**Font**](Font.md) |  | [optional] |
| **legend_value_color** | **str** |  | [optional] |
| **xaxis** | [**TimeSeriesChartXAxisSettings**](TimeSeriesChartXAxisSettings.md) |  | [optional] |
| **yaxes** | [**Dict[str, TimeSeriesChartYAxisSettings]**](TimeSeriesChartYAxisSettings.md) |  | [optional] |
| **thresholds** | [**List[TimeSeriesChartThreshold]**](TimeSeriesChartThreshold.md) |  | [optional] |
| **grid** | [**TimeSeriesChartGridSettings**](TimeSeriesChartGridSettings.md) |  | [optional] |
| **y_axes** | [**Dict[str, TimeSeriesChartYAxisSettings]**](TimeSeriesChartYAxisSettings.md) |  | [optional] |
| **x_axis** | [**TimeSeriesChartXAxisSettings**](TimeSeriesChartXAxisSettings.md) |  | [optional] |
| **bar_width_settings** | [**TimeSeriesChartBarWidthSettings**](TimeSeriesChartBarWidthSettings.md) |  | [optional] |
| **no_aggregation_bar_width_settings** | [**TimeSeriesChartNoAggregationBarWidthSettings**](TimeSeriesChartNoAggregationBarWidthSettings.md) |  | [optional] |
| **states** | [**List[TimeSeriesChartStateSettings]**](TimeSeriesChartStateSettings.md) |  | [optional] |
| **comparison_x_axis** | [**TimeSeriesChartXAxisSettings**](TimeSeriesChartXAxisSettings.md) |  | [optional] |
| **legend_config** | [**LegendConfig**](LegendConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.show_title`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportTimeSeriesChartSettings.model_validate(data)` or `ReportTimeSeriesChartSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

