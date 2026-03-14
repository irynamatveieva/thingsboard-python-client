
# BarSeriesSettings

`tb_pe_client.models.BarSeriesSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_border** | **bool** |  | [optional] |
| **border_width** | **float** |  | [optional] |
| **border_radius** | **float** |  | [optional] |
| **bar_width** | **float** |  | [optional] |
| **show_label** | **bool** |  | [optional] |
| **label_position** | [**ChartLabelPosition**](ChartLabelPosition.md) |  | [optional] |
| **label_font** | [**Font**](Font.md) |  | [optional] |
| **label_color** | **str** |  | [optional] |
| **enable_label_background** | **bool** |  | [optional] |
| **label_background** | **str** |  | [optional] |
| **background_settings** | [**ChartFillSettings**](ChartFillSettings.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.show_border`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BarSeriesSettings.model_validate(data)` or `BarSeriesSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

