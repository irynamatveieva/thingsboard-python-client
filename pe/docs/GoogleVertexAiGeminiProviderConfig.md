
# GoogleVertexAiGeminiProviderConfig

`tb_pe_client.models.GoogleVertexAiGeminiProviderConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **file_name** | **str** |  | [optional] |
| **project_id** | **str** |  | |
| **location** | **str** |  | |
| **service_account_key** | **str** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.file_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `GoogleVertexAiGeminiProviderConfig.model_validate(data)` or `GoogleVertexAiGeminiProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

