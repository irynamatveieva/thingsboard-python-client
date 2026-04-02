
# AggregationParams

`tb_pe_client.models.AggregationParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **aggregation** | [**Aggregation**](Aggregation.md) |  | [optional] |
| **interval_type** | [**IntervalType**](IntervalType.md) |  | [optional] |
| **tz_id** | **str** |  | [optional] |
| **interval** | **int** |  | [optional] |



## Referenced Types

#### Aggregation (enum)
`MIN` | `MAX` | `AVG` | `SUM` | `COUNT` | `NONE`

#### IntervalType (enum)
`MILLISECONDS` | `WEEK` | `WEEK_ISO` | `MONTH` | `QUARTER`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.aggregation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AggregationParams.model_validate(data)` or `AggregationParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

