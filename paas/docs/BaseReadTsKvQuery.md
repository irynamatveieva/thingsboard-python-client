
# BaseReadTsKvQuery

`tb_paas_client.models.BaseReadTsKvQuery`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **int** |  | [optional] |
| **key** | **str** |  | [optional] |
| **start_ts** | **int** |  | [optional] |
| **end_ts** | **int** |  | [optional] |
| **agg_parameters** | [**AggregationParams**](AggregationParams.md) |  | [optional] |
| **limit** | **int** |  | [optional] |
| **order** | **str** |  | [optional] |
| **aggregation** | [**Aggregation**](Aggregation.md) |  | [optional] |
| **interval** | **int** |  | [optional] |



## Referenced Types

#### AggregationParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| aggregation | Aggregation |  | [optional] |
| interval_type | IntervalType |  | [optional] |
| tz_id | str |  | [optional] |
| interval | int |  | [optional] |

#### Aggregation (enum)
`MIN` | `MAX` | `AVG` | `SUM` | `COUNT` | `NONE`

#### IntervalType (enum)
`MILLISECONDS` | `WEEK` | `WEEK_ISO` | `MONTH` | `QUARTER`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BaseReadTsKvQuery.model_validate(data)` or `BaseReadTsKvQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

