
# ReportBarChartWithLabelsSettings

`tb_pe_client.models.ReportBarChartWithLabelsSettings`

**Extends:** **ReportTimeSeriesChartSettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_bar_label** | **bool** |  | [optional] |
| **bar_label_font** | [**Font**](Font.md) |  | [optional] |
| **bar_label_color** | **str** |  | [optional] |
| **show_bar_value** | **bool** |  | [optional] |
| **bar_value_font** | [**Font**](Font.md) |  | [optional] |
| **bar_value_color** | **str** |  | [optional] |
| **show_bar_border** | **bool** |  | [optional] |
| **bar_border_width** | **float** |  | [optional] |
| **bar_border_radius** | **float** |  | [optional] |
| **bar_background_settings** | [**ChartFillSettings**](ChartFillSettings.md) |  | [optional] |
| **bar_units** | **str** |  | [optional] |
| **bar_decimals** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.show_bar_label`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportBarChartWithLabelsSettings.model_validate(data)` or `ReportBarChartWithLabelsSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

