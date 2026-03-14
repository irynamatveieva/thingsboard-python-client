
# AiChatModelConfigObject

`tb_ce_client.models.AiChatModelConfigObject`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **model_type** | [**AiModelType**](AiModelType.md) |  | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.model_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AiChatModelConfigObject.model_validate(data)` or `AiChatModelConfigObject.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

