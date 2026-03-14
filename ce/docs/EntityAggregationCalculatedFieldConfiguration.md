
# EntityAggregationCalculatedFieldConfiguration

`tb_ce_client.models.EntityAggregationCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **metrics** | [**Dict[str, AggMetric]**](AggMetric.md) |  | |
| **interval** | [**AggInterval**](AggInterval.md) |  | |
| **watermark** | [**Watermark**](Watermark.md) |  | [optional] |
| **produce_intermediate_result** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityAggregationCalculatedFieldConfiguration.model_validate(data)` or `EntityAggregationCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

