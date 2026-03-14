
# AggMetric

`tb_paas_client.models.AggMetric`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **function** | [**AggFunction**](AggFunction.md) |  | [optional] |
| **filter** | **str** |  | [optional] |
| **input** | [**AggInput**](AggInput.md) |  | [optional] |
| **default_value** | **float** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.function`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AggMetric.model_validate(data)` or `AggMetric.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

