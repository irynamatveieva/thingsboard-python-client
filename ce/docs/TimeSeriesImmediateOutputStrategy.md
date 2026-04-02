
# TimeSeriesImmediateOutputStrategy

`tb_ce_client.models.TimeSeriesImmediateOutputStrategy`

**Extends:** **TimeSeriesOutputStrategy**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **ttl** | **int** |  | [optional] |
| **save_time_series** | **bool** |  | [optional] |
| **save_latest** | **bool** |  | [optional] |
| **send_ws_update** | **bool** |  | [optional] |
| **process_cfs** | **bool** |  | [optional] |



## Referenced Types

#### TimeSeriesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TimeSeriesRuleChainOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`RULE_CHAIN`)*
*See TimeSeriesOutputStrategy for properties.*

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.ttl`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesImmediateOutputStrategy.model_validate(data)` or `TimeSeriesImmediateOutputStrategy.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

