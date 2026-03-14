
# AiModelConfig

`tb_ce_client.models.AiModelConfig`

Root configuration for AI models

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider** | **str** |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.provider`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AiModelConfig.model_validate(data)` or `AiModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

