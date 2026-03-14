
# OAuth2ClientInfo

`tb_paas_client.models.OAuth2ClientInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**OAuth2ClientId**](OAuth2ClientId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **title** | **str** | Oauth2 client registration title (e.g. My google) | [optional] |
| **provider_name** | **str** | Oauth2 client provider name (e.g. Google) | [optional] |
| **platforms** | [**List[PlatformType]**](PlatformType.md) | List of platforms for which usage of the OAuth2 client is allowed (empty for all allowed) | [optional] |
| **name** | **str** |  | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2ClientInfo.model_validate(data)` or `OAuth2ClientInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

