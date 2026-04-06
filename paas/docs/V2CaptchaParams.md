
# V2CaptchaParams

`tb_paas_client.models.V2CaptchaParams`

**Extends:** **CaptchaParams**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **site_key** | **str** | Captcha site key for 'I'm not a robot' validation | [optional] |
| **log_action_name** | **str** | Optional action name used for logging (for captcha version 'v3' and 'enterprise') | [optional] |
| **secret_key** | **str** | Secret key to validate the Captcha. Should match the Captcha Site Key. | [optional] |



## Referenced Types

#### CaptchaParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.site_key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `V2CaptchaParams.model_validate(data)` or `V2CaptchaParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

