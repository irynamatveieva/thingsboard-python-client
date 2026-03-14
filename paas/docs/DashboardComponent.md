
# DashboardComponent

`tb_paas_client.models.DashboardComponent`

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
| **config** | [**DashboardReportConfig**](DashboardReportConfig.md) | Dashboard report configuration. | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data_sources`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DashboardComponent.model_validate(data)` or `DashboardComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

