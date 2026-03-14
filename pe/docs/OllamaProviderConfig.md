
# OllamaProviderConfig

`tb_pe_client.models.OllamaProviderConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **base_url** | **str** |  | |
| **auth** | [**OllamaAuth**](OllamaAuth.md) |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.base_url`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OllamaProviderConfig.model_validate(data)` or `OllamaProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

