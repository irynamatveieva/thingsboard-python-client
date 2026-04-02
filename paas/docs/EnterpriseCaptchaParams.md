
# EnterpriseCaptchaParams

`tb_paas_client.models.EnterpriseCaptchaParams`

**Extends:** **CaptchaParams**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **project_id** | **str** | Your Google Cloud project ID | [optional] |
| **service_account_credentials** | **str** | Service account credentials | [optional] |
| **service_account_credentials_file_name** | **str** | Service account credentials file name | [optional] |
| **android_key** | **str** | The reCAPTCHA key associated with android app. | [optional] |
| **ios_key** | **str** | The reCAPTCHA key associated with iOS app. | [optional] |
| **log_action_name** | **str** | Optional action name used for logging | [optional] |



## Referenced Types

#### CaptchaParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.project_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EnterpriseCaptchaParams.model_validate(data)` or `EnterpriseCaptchaParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

