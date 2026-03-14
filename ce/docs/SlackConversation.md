
# SlackConversation

`tb_ce_client.models.SlackConversation`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**SlackConversationType**](SlackConversationType.md) |  | |
| **id** | **str** |  | |
| **name** | **str** |  | |
| **whole_name** | **str** |  | [optional] |
| **email** | **str** |  | [optional] |
| **title** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SlackConversation.model_validate(data)` or `SlackConversation.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

