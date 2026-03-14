
# AnthropicChatModelConfig

`tb_ce_client.models.AnthropicChatModelConfig`

**Extends:** **AiModelConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **model_type** | [**AiModelType**](AiModelType.md) |  | [optional] [readonly] |
| **provider_config** | [**AnthropicProviderConfig**](AnthropicProviderConfig.md) |  | |
| **model_id** | **str** |  | |
| **temperature** | **float** |  | [optional] |
| **top_p** | **float** |  | [optional] |
| **top_k** | **int** |  | [optional] |
| **max_output_tokens** | **int** |  | [optional] |
| **timeout_seconds** | **int** |  | [optional] |
| **max_retries** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.model_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AnthropicChatModelConfig.model_validate(data)` or `AnthropicChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

