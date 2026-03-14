
# DynamicValueDouble

`tb_ce_client.models.DynamicValueDouble`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **source_type** | [**DynamicValueSourceType**](DynamicValueSourceType.md) |  | [optional] |
| **source_attribute** | **str** |  | [optional] |
| **inherit** | **bool** |  | [optional] |
| **resolved_value** | **float** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.source_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DynamicValueDouble.model_validate(data)` or `DynamicValueDouble.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

