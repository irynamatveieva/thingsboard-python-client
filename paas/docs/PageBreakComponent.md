
# PageBreakComponent

`tb_paas_client.models.PageBreakComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|



## Referenced Types

#### ReportComponent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sub_type | ReportComponentSubType |  |  |
| type | ReportComponentType |  |  |

#### ReportComponentSubType (enum)
`DOUGHNUTCHART` | `HORIZONTALDOUGHNUTCHART` | `POINTCHART` | `BARCHART` | `PIECHART` | `LINECHART` | `LATESTBARCHART` | `RANGECHART` | `BARCHARTWITHLABELS` | `STATECHART` | … (11 values total)

#### ReportComponentType (enum)
`HEADING` | `RICH_TEXT` | `ENTITY_TABLE` | `TIME_SERIES_TABLE` | `ALARM_TABLE` | `TIME_SERIES_CHART` | `LATEST_CHART` | `DASHBOARD` | `IMAGE` | `SUB_REPORT` | … (14 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageBreakComponent.model_validate(data)` or `PageBreakComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

