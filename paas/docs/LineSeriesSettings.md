
# LineSeriesSettings

`tb_paas_client.models.LineSeriesSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_line** | **bool** |  | [optional] |
| **step** | **bool** |  | [optional] |
| **step_type** | [**LineSeriesStepType**](LineSeriesStepType.md) |  | [optional] |
| **smooth** | **bool** |  | [optional] |
| **line_type** | [**ChartLineType**](ChartLineType.md) |  | [optional] |
| **line_width** | **float** |  | [optional] |
| **show_points** | **bool** |  | [optional] |
| **show_point_label** | **bool** |  | [optional] |
| **point_label_position** | [**ChartLabelPosition**](ChartLabelPosition.md) |  | [optional] |
| **point_label_font** | [**Font**](Font.md) |  | [optional] |
| **point_label_color** | **str** |  | [optional] |
| **enable_point_label_background** | **bool** |  | [optional] |
| **point_label_background** | **str** |  | [optional] |
| **point_shape** | [**ChartShape**](ChartShape.md) |  | [optional] |
| **point_size** | **float** |  | [optional] |
| **fill_area_settings** | [**ChartFillSettings**](ChartFillSettings.md) |  | [optional] |



## Referenced Types

#### LineSeriesStepType (enum)
`START` | `MIDDLE` | `END`

#### ChartLineType (enum)
`SOLID` | `DASHED` | `DOTTED`

#### ChartLabelPosition (enum)
`TOP` | `BOTTOM`

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### ChartShape (enum)
`EMPTYCIRCLE` | `CIRCLE` | `RECT` | `ROUNDRECT` | `TRIANGLE` | `DIAMOND` | `PIN` | `ARROW` | `NONE`

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
- **Attribute access:** `obj.show_line`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LineSeriesSettings.model_validate(data)` or `LineSeriesSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

