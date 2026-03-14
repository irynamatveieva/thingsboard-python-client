
# ConvertersInfo

`tb_pe_client.models.ConvertersInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **library** | **bool** |  | [optional] |
| **existing** | **bool** |  | [optional] |
| **keys** | **List[str]** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.library`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ConvertersInfo.model_validate(data)` or `ConvertersInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

