
# ReportPieChartSettings

`tb_pe_client.models.ReportPieChartSettings`

**Extends:** **ReportLatestChartSettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_label** | **bool** |  | [optional] |
| **label_position** | [**PieChartLabelPosition**](PieChartLabelPosition.md) |  | [optional] |
| **label_font** | [**Font**](Font.md) |  | [optional] |
| **label_color** | **str** |  | [optional] |
| **border_width** | **float** |  | [optional] |
| **border_color** | **str** |  | [optional] |
| **radius** | **float** |  | [optional] |
| **clockwise** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.show_label`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportPieChartSettings.model_validate(data)` or `ReportPieChartSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

