
# TimeSeriesChartKeySettings

`tb_pe_client.models.TimeSeriesChartKeySettings`

**Extends:** **DataKeySettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **y_axis_id** | **str** |  | [optional] |
| **show_in_legend** | **bool** |  | [optional] |
| **series_type** | [**TimeSeriesChartSeriesType**](TimeSeriesChartSeriesType.md) |  | [optional] |
| **line_settings** | [**LineSeriesSettings**](LineSeriesSettings.md) |  | [optional] |
| **bar_settings** | [**BarSeriesSettings**](BarSeriesSettings.md) |  | [optional] |
| **comparison_settings** | [**DataKeyComparisonSettings**](DataKeyComparisonSettings.md) |  | [optional] |
| **yaxis_id** | **str** |  | [optional] |



## Referenced Types

#### DataKeySettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DataKeySettingsType | Data key settings type |  |

#### TimeSeriesChartSeriesType (enum)
`LINE` | `BAR`

#### LineSeriesSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_line | bool |  | [optional] |
| step | bool |  | [optional] |
| step_type | LineSeriesStepType |  | [optional] |
| smooth | bool |  | [optional] |
| line_type | ChartLineType |  | [optional] |
| line_width | float |  | [optional] |
| show_points | bool |  | [optional] |
| show_point_label | bool |  | [optional] |
| point_label_position | ChartLabelPosition |  | [optional] |
| point_label_font | Font |  | [optional] |
| point_label_color | str |  | [optional] |
| enable_point_label_background | bool |  | [optional] |
| point_label_background | str |  | [optional] |
| point_shape | ChartShape |  | [optional] |
| point_size | float |  | [optional] |
| fill_area_settings | ChartFillSettings |  | [optional] |

#### BarSeriesSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_border | bool |  | [optional] |
| border_width | float |  | [optional] |
| border_radius | float |  | [optional] |
| bar_width | float |  | [optional] |
| show_label | bool |  | [optional] |
| label_position | ChartLabelPosition |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| enable_label_background | bool |  | [optional] |
| label_background | str |  | [optional] |
| background_settings | ChartFillSettings |  | [optional] |

#### DataKeyComparisonSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_values_for_comparison | bool |  | [optional] |
| comparison_values_label | str |  | [optional] |
| color | str |  | [optional] |

#### DataKeySettingsType (enum)
`COLUMN` | `TIME_SERIES_CHART` | `DEFAULT`

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

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.y_axis_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesChartKeySettings.model_validate(data)` or `TimeSeriesChartKeySettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

