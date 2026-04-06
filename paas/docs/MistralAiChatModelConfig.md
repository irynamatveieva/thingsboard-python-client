
# MistralAiChatModelConfig

`tb_paas_client.models.MistralAiChatModelConfig`

**Extends:** **AiModelConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **model_type** | [**AiModelType**](AiModelType.md) |  | [optional] [readonly] |
| **provider_config** | [**MistralAiProviderConfig**](MistralAiProviderConfig.md) |  | |
| **model_id** | **str** |  | |
| **temperature** | **float** |  | [optional] |
| **top_p** | **float** |  | [optional] |
| **frequency_penalty** | **float** |  | [optional] |
| **presence_penalty** | **float** |  | [optional] |
| **max_output_tokens** | **int** |  | [optional] |
| **timeout_seconds** | **int** |  | [optional] |
| **max_retries** | **int** |  | [optional] |



## Referenced Types

#### AiModelConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider | str |  |  |

#### AiModelType (enum)
`CHAT`

#### MistralAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.model_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MistralAiChatModelConfig.model_validate(data)` or `MistralAiChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

