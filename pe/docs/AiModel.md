
# AiModel

`tb_pe_client.models.AiModel`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AiModelId**](AiModelId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object representing the ID of the tenant associated with this AI model | [readonly] |
| **version** | **int** | Version of the AI model record; increments automatically whenever the record is changed | [readonly] |
| **name** | **str** | Display name for this AI model configuration; not the technical model identifier | |
| **configuration** | [**AiModelConfig**](AiModelConfig.md) | Configuration of the AI model | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AiModel.model_validate(data)` or `AiModel.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

