
# CellSettings

`tb_paas_client.models.CellSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **font** | [**Font**](Font.md) |  | [optional] |
| **color** | **str** |  | [optional] |
| **background_color** | **str** |  | [optional] |
| **text_alignment** | [**TextAlignment**](TextAlignment.md) |  | [optional] |
| **vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.font`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CellSettings.model_validate(data)` or `CellSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

