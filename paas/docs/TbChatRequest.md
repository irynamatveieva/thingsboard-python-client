
# TbChatRequest

`tb_paas_client.models.TbChatRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **system_message** | **str** | A system-level instruction that frames the user's input, setting the persona, tone, and constraints for the generated response | [optional] |
| **user_message** | [**TbUserMessage**](TbUserMessage.md) | The actual user prompt that will be answered by the AI model | |
| **chat_model_config** | [**AiModelConfig**](AiModelConfig.md) | Configuration of the AI chat model that should execute the request | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.system_message`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbChatRequest.model_validate(data)` or `TbChatRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

