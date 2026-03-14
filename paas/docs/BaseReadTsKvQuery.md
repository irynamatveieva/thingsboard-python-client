
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



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BaseReadTsKvQuery.model_validate(data)` or `BaseReadTsKvQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

