
# TimeSeriesOutput

`tb_ce_client.models.TimeSeriesOutput`

**Extends:** **Output**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **strategy** | [**TimeSeriesOutputStrategy**](TimeSeriesOutputStrategy.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.strategy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesOutput.model_validate(data)` or `TimeSeriesOutput.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

