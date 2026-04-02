
# ColumnSettings

`tb_pe_client.models.ColumnSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **column_width** | **str** |  | [optional] |
| **header** | [**CellSettings**](CellSettings.md) |  | [optional] |
| **cell** | [**CellSettings**](CellSettings.md) |  | [optional] |
| **type** | [**DataKeySettingsType**](DataKeySettingsType.md) | Data key settings type | |



## Referenced Types

#### CellSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| font | Font |  | [optional] |
| color | str |  | [optional] |
| background_color | str |  | [optional] |
| text_alignment | TextAlignment |  | [optional] |
| vertical_alignment | VerticalAlignment |  | [optional] |

#### DataKeySettingsType (enum)
`COLUMN` | `TIME_SERIES_CHART` | `DEFAULT`

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### TextAlignment (enum)
`CENTER` | `RIGHT` | `LEFT` | `JUSTIFY`

#### VerticalAlignment (enum)
`BOTTOM` | `TOP` | `MIDDLE`

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.column_width`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ColumnSettings.model_validate(data)` or `ColumnSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

