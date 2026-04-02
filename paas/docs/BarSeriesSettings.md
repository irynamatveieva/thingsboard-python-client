
# BarSeriesSettings

`tb_paas_client.models.BarSeriesSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_border** | **bool** |  | [optional] |
| **border_width** | **float** |  | [optional] |
| **border_radius** | **float** |  | [optional] |
| **bar_width** | **float** |  | [optional] |
| **show_label** | **bool** |  | [optional] |
| **label_position** | [**ChartLabelPosition**](ChartLabelPosition.md) |  | [optional] |
| **label_font** | [**Font**](Font.md) |  | [optional] |
| **label_color** | **str** |  | [optional] |
| **enable_label_background** | **bool** |  | [optional] |
| **label_background** | **str** |  | [optional] |
| **background_settings** | [**ChartFillSettings**](ChartFillSettings.md) |  | [optional] |



## Referenced Types

#### ChartLabelPosition (enum)
`TOP` | `BOTTOM`

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### ChartFillSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ChartFillType |  | [optional] |
| opacity | float |  | [optional] |
| gradient | ChartFillSettingsGradient |  | [optional] |

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

#### ChartFillType (enum)
`NONE` | `OPACITY` | `GRADIENT`

#### ChartFillSettingsGradient
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| start | float |  | [optional] |
| end | float |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.show_border`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BarSeriesSettings.model_validate(data)` or `BarSeriesSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

