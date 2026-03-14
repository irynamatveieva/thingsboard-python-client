
# SplitViewComponent

`tb_paas_client.models.SplitViewComponent`

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
| **left_view** | [**ReportComponent**](ReportComponent.md) |  | [optional] |
| **right_view** | [**ReportComponent**](ReportComponent.md) |  | [optional] |
| **split_position** | **float** |  | [optional] |
| **split_gap** | **int** |  | [optional] |
| **left_vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) |  | [optional] |
| **right_vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.margins`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SplitViewComponent.model_validate(data)` or `SplitViewComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

