
# CaptchaClientParams

`tb_paas_client.models.CaptchaClientParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **captcha_site_key** | **str** |  | [optional] |
| **captcha_version** | **str** |  | [optional] |
| **captcha_action** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.captcha_site_key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CaptchaClientParams.model_validate(data)` or `CaptchaClientParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

