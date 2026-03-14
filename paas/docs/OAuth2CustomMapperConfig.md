
# OAuth2CustomMapperConfig

`tb_paas_client.models.OAuth2CustomMapperConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **url** | **str** |  | [optional] |
| **username** | **str** |  | [optional] |
| **password** | **str** |  | [optional] |
| **send_token** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.url`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2CustomMapperConfig.model_validate(data)` or `OAuth2CustomMapperConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

