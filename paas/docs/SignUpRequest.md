
# SignUpRequest

`tb_paas_client.models.SignUpRequest`

A JSON value representing the signup request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **fields** | **Dict[str, str]** | List of sign-up form fields | [optional] |
| **recaptcha_response** | **str** | Response from reCAPTCHA validation | [optional] |
| **pkg_name** | **str** | For mobile apps only. Mobile app package name | [optional] |
| **platform** | [**PlatformType**](PlatformType.md) | For mobile apps only. Mobile app package platform | [optional] |
| **app_secret** | **str** | For mobile apps only. Mobile app secret | [optional] |



## Referenced Types

#### PlatformType (enum)
`WEB` | `ANDROID` | `IOS`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.fields`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SignUpRequest.model_validate(data)` or `SignUpRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

