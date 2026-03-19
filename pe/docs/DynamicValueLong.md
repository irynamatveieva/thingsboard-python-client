
# DynamicValueLong

`tb_pe_client.models.DynamicValueLong`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **resolved_value** | **int** |  | [optional] |
| **source_type** | [**DynamicValueSourceType**](DynamicValueSourceType.md) |  | [optional] |
| **source_attribute** | **str** |  | [optional] |
| **inherit** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.resolved_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DynamicValueLong.model_validate(data)` or `DynamicValueLong.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

