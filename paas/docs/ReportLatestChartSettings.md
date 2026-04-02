
# ReportLatestChartSettings

`tb_paas_client.models.ReportLatestChartSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_title** | **bool** |  | [optional] |
| **title** | **str** |  | [optional] |
| **title_font** | [**Font**](Font.md) |  | [optional] |
| **title_color** | **str** |  | [optional] |
| **title_alignment** | [**TextAlignment**](TextAlignment.md) |  | [optional] |
| **units** | **str** |  | [optional] |
| **decimals** | **int** |  | [optional] |
| **auto_scale** | **bool** |  | [optional] |
| **sort_series** | **bool** |  | [optional] |
| **show_total** | **bool** |  | [optional] |
| **show_legend** | **bool** |  | [optional] |
| **legend_position** | [**LegendPosition**](LegendPosition.md) |  | [optional] |
| **legend_label_font** | [**Font**](Font.md) |  | [optional] |
| **legend_label_color** | **str** |  | [optional] |
| **legend_value_font** | [**Font**](Font.md) |  | [optional] |
| **legend_value_color** | **str** |  | [optional] |
| **legend_show_total** | **bool** |  | [optional] |



## Subtypes

#### ReportDoughnutChartSettings  *(sub_type=`doughnutChart`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| layout | DoughnutLayout |  | [optional] |
| clockwise | bool |  | [optional] |
| total_value_font | Font |  | [optional] |
| total_value_color | str |  | [optional] |

#### ReportDoughnutChartSettings  *(sub_type=`horizontalDoughnutChart`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| layout | DoughnutLayout |  | [optional] |
| clockwise | bool |  | [optional] |
| total_value_font | Font |  | [optional] |
| total_value_color | str |  | [optional] |

#### ReportBarChartSettings  *(sub_type=`latestBarChart`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| axis_min | float |  | [optional] |
| axis_max | float |  | [optional] |
| axis_tick_label_font | Font |  | [optional] |
| axis_tick_label_color | str |  | [optional] |
| bar_settings | BarSeriesSettings |  | [optional] |

#### ReportPieChartSettings  *(sub_type=`pieChart`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_label | bool |  | [optional] |
| label_position | PieChartLabelPosition |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| border_width | float |  | [optional] |
| border_color | str |  | [optional] |
| radius | float |  | [optional] |
| clockwise | bool |  | [optional] |

## Referenced Types

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### TextAlignment (enum)
`CENTER` | `RIGHT` | `LEFT` | `JUSTIFY`

#### LegendPosition (enum)
`TOP` | `BOTTOM` | `LEFT` | `RIGHT`

#### DoughnutLayout (enum)
`DEFAULT` | `WITH_TOTAL`

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

#### PieChartLabelPosition (enum)
`INSIDE` | `OUTSIDE`

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

#### ChartLabelPosition (enum)
`TOP` | `BOTTOM`

#### ChartFillSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ChartFillType |  | [optional] |
| opacity | float |  | [optional] |
| gradient | ChartFillSettingsGradient |  | [optional] |

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
- **Attribute access:** `obj.show_title`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportLatestChartSettings.model_validate(data)` or `ReportLatestChartSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

