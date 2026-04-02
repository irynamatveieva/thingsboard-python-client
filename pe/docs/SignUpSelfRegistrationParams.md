
# SignUpSelfRegistrationParams

`tb_pe_client.models.SignUpSelfRegistrationParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **title** | **str** |  | [optional] |
| **captcha** | [**CaptchaParams**](CaptchaParams.md) |  | [optional] |
| **fields** | [**List[SignUpField]**](SignUpField.md) |  | [optional] |
| **show_privacy_policy** | **bool** |  | [optional] |
| **show_terms_of_use** | **bool** |  | [optional] |



## Referenced Types

#### CaptchaParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version | str |  |  |

#### EnterpriseCaptchaParams  *(extends CaptchaParams, version=`enterprise`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| project_id | str | Your Google Cloud project ID | [optional] |
| service_account_credentials | str | Service account credentials | [optional] |
| service_account_credentials_file_name | str | Service account credentials file name | [optional] |
| android_key | str | The reCAPTCHA key associated with android app. | [optional] |
| ios_key | str | The reCAPTCHA key associated with iOS app. | [optional] |
| log_action_name | str | Optional action name used for logging | [optional] |

#### V2CaptchaParams  *(extends CaptchaParams, version=`v2`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| site_key | str | Captcha site key for 'I'm not a robot' validation | [optional] |
| log_action_name | str | Optional action name used for logging (for captcha version 'v3' and 'enterprise') | [optional] |
| secret_key | str | Secret key to validate the Captcha. Should match the Captcha Site Key. | [optional] |

#### V3CaptchaParams  *(extends CaptchaParams, version=`v3`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| site_key | str | Captcha site key for 'I'm not a robot' validation | [optional] |
| log_action_name | str | Optional action name used for logging (for captcha version 'v3' and 'enterprise') | [optional] |
| secret_key | str | Secret key to validate the Captcha. Should match the Captcha Site Key. | [optional] |

#### SignUpField
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | SignUpFieldId | Signup field id |  |
| label | str | Signup field label |  |
| required | bool | Indicates if field is required | [optional] |

#### SignUpFieldId (enum)
`EMAIL` | `PASSWORD` | `REPEAT_PASSWORD` | `FIRST_NAME` | `LAST_NAME` | `PHONE` | `COUNTRY` | `CITY` | `STATE` | `ZIP` | … (12 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.title`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SignUpSelfRegistrationParams.model_validate(data)` or `SignUpSelfRegistrationParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

