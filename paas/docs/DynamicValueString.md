
# DynamicValueString

`tb_paas_client.models.DynamicValueString`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **source_type** | [**DynamicValueSourceType**](DynamicValueSourceType.md) |  | [optional] |
| **source_attribute** | **str** |  | [optional] |
| **inherit** | **bool** |  | [optional] |
| **resolved_value** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.source_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DynamicValueString.model_validate(data)` or `DynamicValueString.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

