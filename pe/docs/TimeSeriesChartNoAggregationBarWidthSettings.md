
# TimeSeriesChartNoAggregationBarWidthSettings

`tb_pe_client.models.TimeSeriesChartNoAggregationBarWidthSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **strategy** | [**TimeSeriesChartNoAggregationBarWidthStrategy**](TimeSeriesChartNoAggregationBarWidthStrategy.md) |  | [optional] |
| **group_width** | [**TimeSeriesChartBarWidth**](TimeSeriesChartBarWidth.md) |  | [optional] |
| **bar_width** | [**TimeSeriesChartBarWidth**](TimeSeriesChartBarWidth.md) |  | [optional] |



## Referenced Types

#### TimeSeriesChartNoAggregationBarWidthStrategy (enum)
`GROUP` | `SEPARATE`

#### TimeSeriesChartBarWidth
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relative | bool |  | [optional] |
| relative_width | float |  | [optional] |
| absolute_width | float |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.strategy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesChartNoAggregationBarWidthSettings.model_validate(data)` or `TimeSeriesChartNoAggregationBarWidthSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

