
# PaletteSettings

`tb_pe_client.models.PaletteSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **primary_palette** | [**Palette**](Palette.md) | Primary palette JSON | |
| **accent_palette** | [**Palette**](Palette.md) | Accent palette JSON | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.primary_palette`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PaletteSettings.model_validate(data)` or `PaletteSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

