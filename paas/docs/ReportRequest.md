
# ReportRequest

`tb_paas_client.models.ReportRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **report_template_id** | [**ReportTemplateId**](ReportTemplateId.md) | Json object representing the report template id. | [optional] |
| **report_template_config** | [**ReportTemplateConfig**](ReportTemplateConfig.md) | Json object representing the report template config. | [optional] |
| **timezone** | **str** | Timezone used for report generation. | [optional] |
| **user_id** | **str** | A string value representing the user id. | [optional] |
| **originator** | [**EntityId**](EntityId.md) | Json object representing the originator id. | [optional] |
| **targets** | **List[UUID]** |  | [optional] |
| **notification_template_id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`NotificationTemplateId`, `ReportTemplateId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### ReportTemplateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name_pattern | str |  | [optional] |
| time_data_pattern | str |  | [optional] |
| format | TbReportFormat | Report format |  |
| entity_aliases | List[EntityAlias] |  | [optional] |
| filters | List[Filter] |  | [optional] |
| components | List[ReportComponent] |  | [optional] |

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
- **Attribute access:** `obj.report_template_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportRequest.model_validate(data)` or `ReportRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

