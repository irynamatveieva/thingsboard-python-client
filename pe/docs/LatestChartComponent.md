
# LatestChartComponent

`tb_pe_client.models.LatestChartComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data_sources** | [**List[DataSource]**](DataSource.md) |  | [optional] |
| **margins** | [**Insets**](Insets.md) |  | [optional] |
| **paddings** | [**Insets**](Insets.md) |  | [optional] |
| **background** | **str** |  | [optional] |
| **border_width** | **int** |  | [optional] |
| **border_radius** | **int** |  | [optional] |
| **border_color** | **str** |  | [optional] |
| **width_type** | [**ImageWidthType**](ImageWidthType.md) |  | [optional] |
| **custom_width** | **int** |  | [optional] |
| **alignment** | [**ImageAlignment**](ImageAlignment.md) |  | [optional] |
| **height** | **int** |  | [optional] |
| **latest_chart_settings** | [**ReportLatestChartSettings**](ReportLatestChartSettings.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data_sources`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LatestChartComponent.model_validate(data)` or `LatestChartComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

