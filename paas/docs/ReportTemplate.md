
# ReportTemplate

`tb_paas_client.models.ReportTemplate`

A JSON value representing the Report Template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**ReportTemplateId**](ReportTemplateId.md) | JSON object with the report template Id. Specify this field to update the report. Referencing non-existing report template Id will cause error. Omit this field to create new report template | [optional] |
| **created_time** | **int** | Timestamp of the report template creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Tenant Id of the report template can't be changed. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id | [optional] [readonly] |
| **name** | **str** | Report name | |
| **format** | [**TbReportFormat**](TbReportFormat.md) | Report format | |
| **type** | [**ReportTemplateType**](ReportTemplateType.md) | Report template type | |
| **description** | **str** | Description | [optional] |
| **version** | **int** |  | [optional] |
| **configuration** | [**ReportTemplateConfig**](ReportTemplateConfig.md) | a JSON value with report template configuration | |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`CustomerId`, `ReportTemplateId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### TbReportFormat (enum)
`PDF` | `CSV`

#### ReportTemplateType (enum)
`REPORT` | `SUB_REPORT`

#### ReportTemplateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name_pattern | str |  | [optional] |
| time_data_pattern | str |  | [optional] |
| format | TbReportFormat | Report format |  |
| entity_aliases | List[EntityAlias] |  | [optional] |
| filters | List[Filter] |  | [optional] |
| components | List[ReportComponent] |  | [optional] |

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

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

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
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportTemplate.model_validate(data)` or `ReportTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

