
# DashboardComponent

`tb_paas_client.models.DashboardComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data_sources** | [**List[DataSource]**](DataSource.md) |  | [optional] |
| **margins** | [**Insets**](Insets.md) |  | [optional] |
| **paddings** | [**Insets**](Insets.md) |  | [optional] |
| **background** | **str** |  | [optional] |
| **border_width** | **int** |  | [optional] |
| **border_radius** | **int** |  | [optional] |
| **border_color** | **str** |  | [optional] |
| **width_type** | [**ImageWidthType**](ImageWidthType.md) |  | [optional] |
| **custom_width** | **int** |  | [optional] |
| **alignment** | [**ImageAlignment**](ImageAlignment.md) |  | [optional] |
| **config** | [**DashboardReportConfig**](DashboardReportConfig.md) | Dashboard report configuration. | |



## Referenced Types

> **EntityId types** (`UserId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### ReportComponent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sub_type | ReportComponentSubType |  |  |
| type | ReportComponentType |  |  |

#### DataSource
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DataSourceType |  | [optional] |
| device_id | str |  | [optional] |
| entity_alias_id | str |  | [optional] |
| filter_id | str |  | [optional] |
| data_keys | List[DataKey] |  | [optional] |
| latest_data_keys | List[DataKey] |  | [optional] |
| alarm_filter_config | AlarmFilterConfig |  | [optional] |

#### Insets
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| left | int |  | [optional] |
| right | int |  | [optional] |
| top | int |  | [optional] |
| bottom | int |  | [optional] |

#### ImageWidthType (enum)
`FITWIDTH` | `ORIGINAL` | `CUSTOM`

#### ImageAlignment (enum)
`LEFT` | `CENTER` | `RIGHT`

#### DashboardReportConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str | Base URL of ThingsBoard UI that should be accessible by Web Report Server. |  |
| dashboard_id | str | A string value representing the dashboard id. |  |
| state | str | Target dashboard state for dashboard report generation. | [optional] |
| timezone | str | Timezone in which target dashboard will be presented in dashboard report. |  |
| use_dashboard_timewindow | bool | If set, timewindow configured in the target dashboard will be used during dashboard report generation. | [optional] |
| timewindow | object | Specific dashboard timewindow that will be used during dashboard report generation. | [optional] |
| name_pattern | str | If set, timewindow configured in the target dashboard will be used during dashboard report generation. |  |
| type | str | Dashboard report file type, can be PDF | PNG |
| use_current_user_credentials | bool | If set, credentials of user created this dashboard report configuration will be used to open dashboard UI during dashboard report generation. | [optional] |
| user_id | str | A string value representing the user id. |  |

#### ReportComponentSubType (enum)
`DOUGHNUTCHART` | `HORIZONTALDOUGHNUTCHART` | `POINTCHART` | `BARCHART` | `PIECHART` | `LINECHART` | `LATESTBARCHART` | `RANGECHART` | `BARCHARTWITHLABELS` | `STATECHART` | … (11 values total)

#### ReportComponentType (enum)
`HEADING` | `RICH_TEXT` | `ENTITY_TABLE` | `TIME_SERIES_TABLE` | `ALARM_TABLE` | `TIME_SERIES_CHART` | `LATEST_CHART` | `DASHBOARD` | `IMAGE` | `SUB_REPORT` | … (14 values total)

#### DataSourceType (enum)
`DEVICE` | `ENTITY` | `ENTITYCOUNT` | `ALARMCOUNT`

#### DataKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str |  | [optional] |
| type | str |  | [optional] |
| label | str |  | [optional] |
| color | str |  | [optional] |
| decimals | int |  | [optional] |
| units | str |  | [optional] |
| aggregation_type | Aggregation |  | [optional] |
| timewindow | TimeWindowConfiguration |  | [optional] |
| use_post_processing | bool |  | [optional] |
| post_func_body | str |  | [optional] |
| settings | DataKeySettings |  | [optional] |

#### AlarmFilterConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type_list | List[str] |  | [optional] |
| status_list | List[AlarmSearchStatus] |  | [optional] |
| severity_list | List[AlarmSeverity] |  | [optional] |
| assignee_id | UserId |  | [optional] |
| search_propagated_alarms | bool |  | [optional] |

#### Aggregation (enum)
`MIN` | `MAX` | `AVG` | `SUM` | `COUNT` | `NONE`

#### TimeWindowConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| history | History |  | [optional] |
| aggregation | AggregationConfiguration |  | [optional] |
| timezone | str |  | [optional] |

#### DataKeySettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DataKeySettingsType | Data key settings type |  |

#### AlarmSearchStatus (enum)
`ANY` | `ACTIVE` | `CLEARED` | `ACK` | `UNACK`

#### AlarmSeverity (enum)
`CRITICAL` | `MAJOR` | `MINOR` | `WARNING` | `INDETERMINATE`

#### History
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| history_type | int |  | [optional] |
| interval | Interval |  | [optional] |
| timewindow_ms | int |  | [optional] |
| fixed_timewindow | FixedTimeWindow |  | [optional] |
| quick_interval | QuickTimeInterval |  | [optional] |

#### AggregationConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | Aggregation |  | [optional] |
| limit | int |  | [optional] |

#### DataKeySettingsType (enum)
`COLUMN` | `TIME_SERIES_CHART` | `DEFAULT`

#### Interval
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| interval | int |  | [optional] |
| interval_type | IntervalType |  | [optional] |

#### FixedTimeWindow
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| start_time_ms | int |  | [optional] |
| end_time_ms | int |  | [optional] |

#### QuickTimeInterval (enum)
`YESTERDAY` | `DAY_BEFORE_YESTERDAY` | `THIS_DAY_LAST_WEEK` | `PREVIOUS_WEEK` | `PREVIOUS_WEEK_ISO` | `PREVIOUS_MONTH` | `PREVIOUS_QUARTER` | `PREVIOUS_HALF_YEAR` | `PREVIOUS_YEAR` | `CURRENT_HOUR` | … (24 values total)

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### IntervalType (enum)
`MILLISECONDS` | `WEEK` | `WEEK_ISO` | `MONTH` | `QUARTER`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data_sources`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DashboardComponent.model_validate(data)` or `DashboardComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

