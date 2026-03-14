
# TimeseriesTableComponent

`tb_pe_client.models.TimeseriesTableComponent`

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
| **show_table_heading** | **bool** |  | [optional] |
| **table_heading** | [**Heading**](Heading.md) |  | [optional] |
| **table_sort_order** | [**TableSortOrder**](TableSortOrder.md) |  | [optional] |
| **timewindow** | [**TimeWindowConfiguration**](TimeWindowConfiguration.md) |  | [optional] |
| **show_timestamp** | **bool** |  | [optional] |
| **timestamp_label** | **str** |  | [optional] |
| **timestamp_pattern** | **str** |  | [optional] |
| **timestamp_column_settings** | [**ColumnSettings**](ColumnSettings.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data_sources`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeseriesTableComponent.model_validate(data)` or `TimeseriesTableComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

