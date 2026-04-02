
# ReportBarChartWithLabelsSettings

`tb_paas_client.models.ReportBarChartWithLabelsSettings`

**Extends:** **ReportTimeSeriesChartSettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_bar_label** | **bool** |  | [optional] |
| **bar_label_font** | [**Font**](Font.md) |  | [optional] |
| **bar_label_color** | **str** |  | [optional] |
| **show_bar_value** | **bool** |  | [optional] |
| **bar_value_font** | [**Font**](Font.md) |  | [optional] |
| **bar_value_color** | **str** |  | [optional] |
| **show_bar_border** | **bool** |  | [optional] |
| **bar_border_width** | **float** |  | [optional] |
| **bar_border_radius** | **float** |  | [optional] |
| **bar_background_settings** | [**ChartFillSettings**](ChartFillSettings.md) |  | [optional] |
| **bar_units** | **str** |  | [optional] |
| **bar_decimals** | **int** |  | [optional] |



## Referenced Types

#### ReportTimeSeriesChartSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_title | bool |  | [optional] |
| title | str |  | [optional] |
| title_font | Font |  | [optional] |
| title_color | str |  | [optional] |
| title_alignment | TextAlignment |  | [optional] |
| thresholds | List[TimeSeriesChartThreshold] |  | [optional] |
| stack | bool |  | [optional] |
| grid | TimeSeriesChartGridSettings |  | [optional] |
| y_axes | Dict[str, TimeSeriesChartYAxisSettings] |  | [optional] |
| x_axis | TimeSeriesChartXAxisSettings |  | [optional] |
| bar_width_settings | TimeSeriesChartBarWidthSettings |  | [optional] |
| no_aggregation_bar_width_settings | TimeSeriesChartNoAggregationBarWidthSettings |  | [optional] |
| states | List[TimeSeriesChartStateSettings] |  | [optional] |
| comparison_enabled | bool |  | [optional] |
| time_for_comparison | ComparisonDuration |  | [optional] |
| comparison_custom_interval_value | int |  | [optional] |
| comparison_x_axis | TimeSeriesChartXAxisSettings |  | [optional] |
| show_legend | bool |  | [optional] |
| legend_column_title_font | Font |  | [optional] |
| legend_column_title_color | str |  | [optional] |
| legend_label_font | Font |  | [optional] |
| legend_label_color | str |  | [optional] |
| legend_value_font | Font |  | [optional] |
| legend_value_color | str |  | [optional] |
| legend_config | LegendConfig |  | [optional] |
| xaxis | TimeSeriesChartXAxisSettings |  | [optional] |
| yaxes | Dict[str, TimeSeriesChartYAxisSettings] |  | [optional] |

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

#### TextAlignment (enum)
`CENTER` | `RIGHT` | `LEFT` | `JUSTIFY`

#### TimeSeriesChartThreshold
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ValueSourceType |  | [optional] |
| value | float |  | [optional] |
| latest_key_type | str |  | [optional] |
| latest_key | str |  | [optional] |
| entity_key_type | str |  | [optional] |
| entity_alias | str |  | [optional] |
| entity_key | str |  | [optional] |
| y_axis_id | str |  | [optional] |
| units | str |  | [optional] |
| decimals | int |  | [optional] |
| line_color | str |  | [optional] |
| line_type | ChartLineType |  | [optional] |
| line_width | float |  | [optional] |
| start_symbol | ChartShape |  | [optional] |
| start_symbol_size | float |  | [optional] |
| end_symbol | ChartShape |  | [optional] |
| end_symbol_size | float |  | [optional] |
| show_label | bool |  | [optional] |
| label_position | ThresholdLabelPosition |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| enable_label_background | bool |  | [optional] |
| label_background | str |  | [optional] |
| yaxis_id | str |  | [optional] |

#### TimeSeriesChartGridSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show | bool |  | [optional] |
| background_color | str |  | [optional] |
| border_width | float |  | [optional] |
| border_color | str |  | [optional] |

#### TimeSeriesChartYAxisSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show | bool |  | [optional] |
| label | str |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| position | AxisPosition |  | [optional] |
| show_tick_labels | bool |  | [optional] |
| tick_label_font | Font |  | [optional] |
| tick_label_color | str |  | [optional] |
| show_ticks | bool |  | [optional] |
| ticks_color | str |  | [optional] |
| show_line | bool |  | [optional] |
| line_color | str |  | [optional] |
| show_split_lines | bool |  | [optional] |
| split_lines_color | str |  | [optional] |
| id | str |  | [optional] |
| order | int |  | [optional] |
| units | str |  | [optional] |
| decimals | int |  | [optional] |
| interval | float |  | [optional] |
| split_number | int |  | [optional] |
| min | float |  | [optional] |
| max | float |  | [optional] |

#### TimeSeriesChartXAxisSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show | bool |  | [optional] |
| label | str |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| position | AxisPosition |  | [optional] |
| show_tick_labels | bool |  | [optional] |
| tick_label_font | Font |  | [optional] |
| tick_label_color | str |  | [optional] |
| show_ticks | bool |  | [optional] |
| ticks_color | str |  | [optional] |
| show_line | bool |  | [optional] |
| line_color | str |  | [optional] |
| show_split_lines | bool |  | [optional] |
| split_lines_color | str |  | [optional] |
| ticks_format | Dict[str, str] |  | [optional] |

#### TimeSeriesChartBarWidthSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| bar_gap | float |  | [optional] |
| interval_gap | float |  | [optional] |

#### TimeSeriesChartNoAggregationBarWidthSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | TimeSeriesChartNoAggregationBarWidthStrategy |  | [optional] |
| group_width | TimeSeriesChartBarWidth |  | [optional] |
| bar_width | TimeSeriesChartBarWidth |  | [optional] |

#### TimeSeriesChartStateSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| label | str |  | [optional] |
| value | float |  | [optional] |
| source_type | TimeSeriesChartStateSourceType |  | [optional] |
| source_value | object |  | [optional] |
| source_range_from | float |  | [optional] |
| source_range_to | float |  | [optional] |

#### ComparisonDuration (enum)
`PREVIOUSINTERVAL` | `DAYS` | `WEEKS` | `MONTHS` | `YEARS` | `CUSTOMINTERVAL`

#### LegendConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| position | LegendPosition |  | [optional] |
| sort_data_keys | bool |  | [optional] |
| show_min | bool |  | [optional] |
| show_max | bool |  | [optional] |
| show_avg | bool |  | [optional] |
| show_total | bool |  | [optional] |
| show_latest | bool |  | [optional] |

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

#### ValueSourceType (enum)
`CONSTANT` | `LATESTKEY` | `ENTITY`

#### ChartLineType (enum)
`SOLID` | `DASHED` | `DOTTED`

#### ChartShape (enum)
`EMPTYCIRCLE` | `CIRCLE` | `RECT` | `ROUNDRECT` | `TRIANGLE` | `DIAMOND` | `PIN` | `ARROW` | `NONE`

#### ThresholdLabelPosition (enum)
`START` | `MIDDLE` | `END` | `INSIDESTART` | `INSIDESTARTTOP` | `INSIDESTARTBOTTOM` | `INSIDEMIDDLE` | `INSIDEMIDDLETOP` | `INSIDEMIDDLEBOTTOM` | `INSIDEEND` | … (12 values total)

#### AxisPosition (enum)
`LEFT` | `RIGHT` | `TOP` | `BOTTOM`

#### TimeSeriesChartNoAggregationBarWidthStrategy (enum)
`GROUP` | `SEPARATE`

#### TimeSeriesChartBarWidth
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relative | bool |  | [optional] |
| relative_width | float |  | [optional] |
| absolute_width | float |  | [optional] |

#### TimeSeriesChartStateSourceType (enum)
`CONSTANT` | `RANGE`

#### LegendPosition (enum)
`TOP` | `BOTTOM` | `LEFT` | `RIGHT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.show_bar_label`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportBarChartWithLabelsSettings.model_validate(data)` or `ReportBarChartWithLabelsSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

