
# Insets

`tb_pe_client.models.Insets`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **left** | **int** |  | [optional] |
| **right** | **int** |  | [optional] |
| **top** | **int** |  | [optional] |
| **bottom** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.left`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Insets.model_validate(data)` or `Insets.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

