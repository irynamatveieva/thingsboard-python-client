
# History

`tb_paas_client.models.History`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **history_type** | **int** |  | [optional] |
| **interval** | [**Interval**](Interval.md) |  | [optional] |
| **timewindow_ms** | **int** |  | [optional] |
| **fixed_timewindow** | [**FixedTimeWindow**](FixedTimeWindow.md) |  | [optional] |
| **quick_interval** | [**QuickTimeInterval**](QuickTimeInterval.md) |  | [optional] |



## Referenced Types

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

#### IntervalType (enum)
`MILLISECONDS` | `WEEK` | `WEEK_ISO` | `MONTH` | `QUARTER`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.history_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `History.model_validate(data)` or `History.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

