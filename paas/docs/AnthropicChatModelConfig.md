
# AnthropicChatModelConfig

`tb_paas_client.models.AnthropicChatModelConfig`

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



## Referenced Types

#### AiModelConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider | str |  |  |

#### AmazonBedrockChatModelConfig  *(extends AiModelConfig, provider=`AMAZON_BEDROCK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | AmazonBedrockProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### AzureOpenAiChatModelConfig  *(extends AiModelConfig, provider=`AZURE_OPENAI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | AzureOpenAiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### GitHubModelsChatModelConfig  *(extends AiModelConfig, provider=`GITHUB_MODELS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | GitHubModelsProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### GoogleAiGeminiChatModelConfig  *(extends AiModelConfig, provider=`GOOGLE_AI_GEMINI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | GoogleAiGeminiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| top_k | int |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### GoogleVertexAiGeminiChatModelConfig  *(extends AiModelConfig, provider=`GOOGLE_VERTEX_AI_GEMINI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | GoogleVertexAiGeminiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| top_k | int |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### MistralAiChatModelConfig  *(extends AiModelConfig, provider=`MISTRAL_AI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | MistralAiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### OllamaChatModelConfig  *(extends AiModelConfig, provider=`OLLAMA`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | OllamaProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| top_k | int |  | [optional] |
| context_length | int |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### OpenAiChatModelConfig  *(extends AiModelConfig, provider=`OPENAI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| model_type | AiModelType |  | [optional] [readonly] |
| provider_config | OpenAiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |

#### AiModelType (enum)
`CHAT`

#### AnthropicProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### OpenAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str |  | [optional] |
| api_key | str |  | [optional] |

#### AzureOpenAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| endpoint | str |  |  |
| service_version | str |  | [optional] |
| api_key | str |  |  |

#### GoogleAiGeminiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### GoogleVertexAiGeminiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| file_name | str |  | [optional] |
| project_id | str |  |  |
| location | str |  |  |
| service_account_key | str |  |  |

#### MistralAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### AmazonBedrockProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| region | str |  |  |
| access_key_id | str |  |  |
| secret_access_key | str |  |  |

#### GitHubModelsProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| personal_access_token | str |  |  |

#### OllamaProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str |  |  |
| auth | OllamaAuth |  |  |

#### OllamaAuth
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### Basic  *(extends OllamaAuth, type=`BASIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| username | str |  |  |
| password | str |  |  |

#### ModelNone  *(extends OllamaAuth, type=`NONE`)*
*See OllamaAuth for properties.*

#### Token  *(extends OllamaAuth, type=`TOKEN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| token | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.model_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AnthropicChatModelConfig.model_validate(data)` or `AnthropicChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

