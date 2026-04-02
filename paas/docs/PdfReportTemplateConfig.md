
# PdfReportTemplateConfig

`tb_paas_client.models.PdfReportTemplateConfig`

**Extends:** **ReportTemplateConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **footer** | [**HeaderFooter**](HeaderFooter.md) |  | [optional] |
| **header** | [**HeaderFooter**](HeaderFooter.md) |  | [optional] |
| **page_background** | **str** |  | [optional] |
| **page_margins** | [**Insets**](Insets.md) |  | [optional] |
| **page_orientation** | [**PageOrientation**](PageOrientation.md) |  | [optional] |
| **page_size** | [**PageSize**](PageSize.md) |  | [optional] |



## Referenced Types

#### ReportTemplateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name_pattern | str |  | [optional] |
| time_data_pattern | str |  | [optional] |
| format | TbReportFormat | Report format |  |
| entity_aliases | List[EntityAlias] |  | [optional] |
| filters | List[Filter] |  | [optional] |
| components | List[ReportComponent] |  | [optional] |

#### HeaderFooter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| components | List[ReportComponent] |  |  |
| first_page | object |  | [optional] |

#### Insets
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| left | int |  | [optional] |
| right | int |  | [optional] |
| top | int |  | [optional] |
| bottom | int |  | [optional] |

#### PageOrientation (enum)
`PORTRAIT` | `LANDSCAPE`

#### PageSize (enum)
`A4` | `LETTER` | `LEGAL` | `A5` | `A3` | `TABLOID`

#### TbReportFormat (enum)
`PDF` | `CSV`

#### EntityAlias
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str |  | [optional] |
| alias | str |  | [optional] |
| filter | EntityFilter |  | [optional] |

#### Filter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str |  | [optional] |
| filter | str |  | [optional] |
| key_filters | List[KeyFilter] |  | [optional] |

#### ReportComponent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sub_type | ReportComponentSubType |  |  |
| type | ReportComponentType |  |  |

#### EntityFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### KeyFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | EntityKey |  | [optional] |
| value_type | EntityKeyValueType |  | [optional] |
| predicate | KeyFilterPredicate |  | [optional] |

#### ReportComponentSubType (enum)
`DOUGHNUTCHART` | `HORIZONTALDOUGHNUTCHART` | `POINTCHART` | `BARCHART` | `PIECHART` | `LINECHART` | `LATESTBARCHART` | `RANGECHART` | `BARCHARTWITHLABELS` | `STATECHART` | … (11 values total)

#### ReportComponentType (enum)
`HEADING` | `RICH_TEXT` | `ENTITY_TABLE` | `TIME_SERIES_TABLE` | `ALARM_TABLE` | `TIME_SERIES_CHART` | `LATEST_CHART` | `DASHBOARD` | `IMAGE` | `SUB_REPORT` | … (14 values total)

#### EntityKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | EntityKeyType |  | [optional] |
| key | str |  | [optional] |

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### EntityKeyType (enum)
`ATTRIBUTE` | `CLIENT_ATTRIBUTE` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `ALARM_FIELD`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.footer`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PdfReportTemplateConfig.model_validate(data)` or `PdfReportTemplateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

