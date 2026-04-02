
# LoginMobileInfo

`tb_paas_client.models.LoginMobileInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **o_auth2_client_login_infos** | [**List[OAuth2ClientLoginInfo]**](OAuth2ClientLoginInfo.md) |  | [optional] |
| **self_registration_params** | [**SignUpSelfRegistrationParams**](SignUpSelfRegistrationParams.md) |  | [optional] |
| **store_info** | [**StoreInfo**](StoreInfo.md) |  | [optional] |
| **version_info** | [**MobileAppVersionInfo**](MobileAppVersionInfo.md) |  | [optional] |



## Referenced Types

#### OAuth2ClientLoginInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str | OAuth2 client name | [optional] |
| icon | str | Name of the icon, displayed on OAuth2 log in button | [optional] |
| url | str | URI for OAuth2 log in. On HTTP GET request to this URI, it redirects to the OAuth2 provider page | [optional] |

#### SignUpSelfRegistrationParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| title | str |  | [optional] |
| captcha | CaptchaParams |  | [optional] |
| fields | List[SignUpField] |  | [optional] |
| show_privacy_policy | bool |  | [optional] |
| show_terms_of_use | bool |  | [optional] |

#### StoreInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| app_id | str |  | [optional] |
| sha256_cert_fingerprints | str |  | [optional] |
| store_link | str |  | [optional] |

#### MobileAppVersionInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| min_version | str | Minimum supported version | [optional] |
| min_version_release_notes | str | Release notes of minimum supported version | [optional] |
| latest_version | str | Latest supported version | [optional] |
| latest_version_release_notes | str | Release notes of latest supported version | [optional] |

#### CaptchaParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version | str |  |  |

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

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.o_auth2_client_login_infos`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LoginMobileInfo.model_validate(data)` or `LoginMobileInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

