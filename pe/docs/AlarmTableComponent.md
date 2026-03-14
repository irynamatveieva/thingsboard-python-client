
# AlarmTableComponent

`tb_pe_client.models.AlarmTableComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **margins** | [**Insets**](Insets.md) |  | [optional] |
| **paddings** | [**Insets**](Insets.md) |  | [optional] |
| **background** | **str** |  | [optional] |
| **border_width** | **int** |  | [optional] |
| **border_radius** | **int** |  | [optional] |
| **border_color** | **str** |  | [optional] |
| **show_table_heading** | **bool** |  | [optional] |
| **table_heading** | [**Heading**](Heading.md) |  | [optional] |
| **table_sort_order** | [**TableSortOrder**](TableSortOrder.md) |  | [optional] |
| **alarm_source** | [**DataSource**](DataSource.md) |  | [optional] |
| **timewindow** | [**TimeWindowConfiguration**](TimeWindowConfiguration.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.margins`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmTableComponent.model_validate(data)` or `AlarmTableComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

