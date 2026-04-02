
# DynamicValueDouble

`tb_paas_client.models.DynamicValueDouble`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **resolved_value** | **float** |  | [optional] |
| **source_type** | [**DynamicValueSourceType**](DynamicValueSourceType.md) |  | [optional] |
| **source_attribute** | **str** |  | [optional] |
| **inherit** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.resolved_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DynamicValueDouble.model_validate(data)` or `DynamicValueDouble.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

