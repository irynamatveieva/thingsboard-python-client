
# AmazonBedrockProviderConfig

`tb_pe_client.models.AmazonBedrockProviderConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **region** | **str** |  | |
| **access_key_id** | **str** |  | |
| **secret_access_key** | **str** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.region`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AmazonBedrockProviderConfig.model_validate(data)` or `AmazonBedrockProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

