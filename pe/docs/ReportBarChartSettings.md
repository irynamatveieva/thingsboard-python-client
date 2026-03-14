
# ReportBarChartSettings

`tb_pe_client.models.ReportBarChartSettings`

**Extends:** **ReportLatestChartSettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **axis_min** | **float** |  | [optional] |
| **axis_max** | **float** |  | [optional] |
| **axis_tick_label_font** | [**Font**](Font.md) |  | [optional] |
| **axis_tick_label_color** | **str** |  | [optional] |
| **bar_settings** | [**BarSeriesSettings**](BarSeriesSettings.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.axis_min`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportBarChartSettings.model_validate(data)` or `ReportBarChartSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

