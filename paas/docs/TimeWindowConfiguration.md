
# TimeWindowConfiguration

`tb_paas_client.models.TimeWindowConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **history** | [**History**](History.md) |  | [optional] |
| **aggregation** | [**AggregationConfiguration**](AggregationConfiguration.md) |  | [optional] |
| **timezone** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.history`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeWindowConfiguration.model_validate(data)` or `TimeWindowConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

