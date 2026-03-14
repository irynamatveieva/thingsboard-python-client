
# AzureOpenAiProviderConfig

`tb_ce_client.models.AzureOpenAiProviderConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **endpoint** | **str** |  | |
| **service_version** | **str** |  | [optional] |
| **api_key** | **str** |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.endpoint`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AzureOpenAiProviderConfig.model_validate(data)` or `AzureOpenAiProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

