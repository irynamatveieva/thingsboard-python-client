
# AggInterval

`tb_ce_client.models.AggInterval`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### CustomInterval  *(type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |
| duration_sec | int |  |  |

#### DayInterval  *(type=`DAY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### HourInterval  *(type=`HOUR`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### MonthInterval  *(type=`MONTH`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### QuarterInterval  *(type=`QUARTER`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### WeekInterval  *(type=`WEEK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### WeekSunSatInterval  *(type=`WEEK_SUN_SAT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### YearInterval  *(type=`YEAR`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AggInterval.model_validate(data)` or `AggInterval.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

