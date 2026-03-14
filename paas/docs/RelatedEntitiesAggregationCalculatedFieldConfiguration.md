
# RelatedEntitiesAggregationCalculatedFieldConfiguration

`tb_paas_client.models.RelatedEntitiesAggregationCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **deduplication_interval_in_sec** | **int** |  | [optional] |
| **metrics** | [**Dict[str, AggMetric]**](AggMetric.md) |  | |
| **relation** | [**RelationPathLevel**](RelationPathLevel.md) |  | |
| **scheduled_update_enabled** | **bool** |  | [optional] |
| **scheduled_update_interval** | **int** |  | [optional] |
| **use_latest_ts** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelatedEntitiesAggregationCalculatedFieldConfiguration.model_validate(data)` or `RelatedEntitiesAggregationCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

