
# ReportComponentType

`tb_pe_client.models.ReportComponentType`

## Enum Values


* `HEADING` (value: `'HEADING'`)

* `RICH_TEXT` (value: `'RICH_TEXT'`)

* `ENTITY_TABLE` (value: `'ENTITY_TABLE'`)

* `TIME_SERIES_TABLE` (value: `'TIME_SERIES_TABLE'`)

* `ALARM_TABLE` (value: `'ALARM_TABLE'`)

* `TIME_SERIES_CHART` (value: `'TIME_SERIES_CHART'`)

* `LATEST_CHART` (value: `'LATEST_CHART'`)

* `DASHBOARD` (value: `'DASHBOARD'`)

* `IMAGE` (value: `'IMAGE'`)

* `SUB_REPORT` (value: `'SUB_REPORT'`)

* `PAGE_BREAK` (value: `'PAGE_BREAK'`)

* `ERROR` (value: `'ERROR'`)

* `DIVIDER` (value: `'DIVIDER'`)

* `SPLIT_VIEW` (value: `'SPLIT_VIEW'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportComponentType.model_validate(data)` or `ReportComponentType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

