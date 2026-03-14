
# RelatedEntitiesAggregationCalculatedFieldConfiguration

`tb_pe_client.models.RelatedEntitiesAggregationCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **relation** | [**RelationPathLevel**](RelationPathLevel.md) |  | |
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **deduplication_interval_in_sec** | **int** |  | [optional] |
| **metrics** | [**Dict[str, AggMetric]**](AggMetric.md) |  | |
| **use_latest_ts** | **bool** |  | [optional] |
| **scheduled_update_interval** | **int** |  | [optional] |
| **scheduled_update_enabled** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.relation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelatedEntitiesAggregationCalculatedFieldConfiguration.model_validate(data)` or `RelatedEntitiesAggregationCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

