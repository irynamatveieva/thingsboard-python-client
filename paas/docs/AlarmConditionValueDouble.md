
# AlarmConditionValueDouble

`tb_paas_client.models.AlarmConditionValueDouble`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **static_value** | **float** |  | [optional] |
| **dynamic_value_argument** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.static_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmConditionValueDouble.model_validate(data)` or `AlarmConditionValueDouble.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

