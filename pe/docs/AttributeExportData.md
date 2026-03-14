
# AttributeExportData

`tb_pe_client.models.AttributeExportData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | **str** |  | [optional] |
| **last_update_ts** | **int** |  | [optional] |
| **boolean_value** | **bool** |  | [optional] |
| **str_value** | **str** |  | [optional] |
| **long_value** | **int** |  | [optional] |
| **double_value** | **float** |  | [optional] |
| **json_value** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AttributeExportData.model_validate(data)` or `AttributeExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

