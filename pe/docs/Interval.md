
# Interval

`tb_pe_client.models.Interval`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **interval** | **int** |  | [optional] |
| **interval_type** | [**IntervalType**](IntervalType.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.interval`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Interval.model_validate(data)` or `Interval.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

