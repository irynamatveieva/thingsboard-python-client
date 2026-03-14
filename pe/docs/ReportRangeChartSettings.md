
# ReportRangeChartSettings

`tb_pe_client.models.ReportRangeChartSettings`

**Extends:** **ReportTimeSeriesChartSettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **range_colors** | [**List[ColorRange]**](ColorRange.md) |  | [optional] |
| **out_of_range_color** | **str** |  | [optional] |
| **show_range_thresholds** | **bool** |  | [optional] |
| **range_threshold** | [**TimeSeriesChartThreshold**](TimeSeriesChartThreshold.md) |  | [optional] |
| **fill_area** | **bool** |  | [optional] |
| **fill_area_opacity** | **float** |  | [optional] |
| **line_settings** | [**LineSeriesSettings**](LineSeriesSettings.md) |  | [optional] |
| **range_units** | **str** |  | [optional] |
| **range_decimals** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.range_colors`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportRangeChartSettings.model_validate(data)` or `ReportRangeChartSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

