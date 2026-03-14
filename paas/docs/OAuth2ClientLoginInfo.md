
# OAuth2ClientLoginInfo

`tb_paas_client.models.OAuth2ClientLoginInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | OAuth2 client name | [optional] |
| **icon** | **str** | Name of the icon, displayed on OAuth2 log in button | [optional] |
| **url** | **str** | URI for OAuth2 log in. On HTTP GET request to this URI, it redirects to the OAuth2 provider page | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2ClientLoginInfo.model_validate(data)` or `OAuth2ClientLoginInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

