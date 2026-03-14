
# Palette

`tb_pe_client.models.Palette`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | Name of the pre-defined palette, or 'custom' | |
| **colors** | **Dict[str, str]** | Mapping of hue identifier number to the rgb(a) color code | [optional] |
| **extends** | **str** | Pre-defined palette name that the custom palette extends | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Palette.model_validate(data)` or `Palette.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

