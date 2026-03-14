
# DividerComponent

`tb_pe_client.models.DividerComponent`

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
| **length** | [**BorderLength**](BorderLength.md) |  | [optional] |
| **border_type** | [**BorderType**](BorderType.md) |  | [optional] |
| **width_px** | **int** |  | [optional] |
| **color** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.margins`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DividerComponent.model_validate(data)` or `DividerComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

