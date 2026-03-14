
# TsKvEntry

`tb_paas_client.models.TsKvEntry`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **ts** | **int** |  | [optional] |
| **value** | **object** |  | [optional] |
| **key** | **str** |  | [optional] |
| **double_value** | **float** |  | [optional] |
| **long_value** | **int** |  | [optional] |
| **boolean_value** | **bool** |  | [optional] |
| **value_as_string** | **str** |  | [optional] |
| **data_type** | [**DataType**](DataType.md) |  | [optional] |
| **json_value** | **str** |  | [optional] |
| **str_value** | **str** |  | [optional] |
| **version** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.ts`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TsKvEntry.model_validate(data)` or `TsKvEntry.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

