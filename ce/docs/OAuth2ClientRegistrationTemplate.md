
# OAuth2ClientRegistrationTemplate

`tb_ce_client.models.OAuth2ClientRegistrationTemplate`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**OAuth2ClientRegistrationTemplateId**](OAuth2ClientRegistrationTemplateId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **provider_id** | **str** | OAuth2 provider identifier (e.g. its name) | |
| **mapper_config** | [**OAuth2MapperConfig**](OAuth2MapperConfig.md) | Default config for mapping OAuth2 log in response to platform entities | [optional] |
| **authorization_uri** | **str** | Default authorization URI of the OAuth2 provider | [optional] |
| **access_token_uri** | **str** | Default access token URI of the OAuth2 provider | [optional] |
| **scope** | **List[str]** | Default OAuth scopes that will be requested from OAuth2 platform | [optional] |
| **user_info_uri** | **str** | Default user info URI of the OAuth2 provider | [optional] |
| **user_name_attribute_name** | **str** | Default name of the username attribute in OAuth2 provider log in response | [optional] |
| **jwk_set_uri** | **str** | Default JSON Web Key URI of the OAuth2 provider | [optional] |
| **client_authentication_method** | **str** | Default client authentication method to use: 'BASIC' or 'POST' | [optional] |
| **comment** | **str** | Comment for OAuth2 provider | [optional] |
| **login_button_icon** | **str** | Default log in button icon for OAuth2 provider | [optional] |
| **login_button_label** | **str** | Default OAuth2 provider label | [optional] |
| **help_link** | **str** | Help link for OAuth2 provider | [optional] |
| **name** | **str** |  | [optional] |
| **additional_info** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2ClientRegistrationTemplate.model_validate(data)` or `OAuth2ClientRegistrationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

