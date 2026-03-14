
# HeadingComponent

`tb_pe_client.models.HeadingComponent`

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
| **value** | **str** |  | [optional] |
| **font** | [**Font**](Font.md) |  | [optional] |
| **color** | **str** |  | [optional] |
| **text_alignment** | [**TextAlignment**](TextAlignment.md) |  | [optional] |
| **vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) |  | [optional] |
| **height** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data_sources`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `HeadingComponent.model_validate(data)` or `HeadingComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

