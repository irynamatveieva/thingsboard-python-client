
# PlatformTwoFaSettings

`tb_paas_client.models.PlatformTwoFaSettings`

Settings value

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **use_system_two_factor_auth_settings** | **bool** |  | [optional] |
| **providers** | [**List[TwoFaProviderConfig]**](TwoFaProviderConfig.md) |  | |
| **min_verification_code_send_period** | **int** |  | |
| **verification_code_check_rate_limit** | **str** |  | [optional] |
| **max_verification_failures_before_user_lockout** | **int** |  | [optional] |
| **total_allowed_time_for_verification** | **int** |  | |
| **enforce_two_fa** | **bool** |  | [optional] |
| **enforced_users_filter** | **object** |  | [optional] |



## Referenced Types

#### TwoFaProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_type | str |  |  |

#### BackupCodeTwoFaProviderConfig  *(extends TwoFaProviderConfig, provider_type=`BACKUP_CODE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| codes_quantity | int |  | [optional] |

#### EmailTwoFaProviderConfig  *(extends TwoFaProviderConfig, provider_type=`EMAIL`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| verification_code_lifetime | int |  | [optional] |

#### SmsTwoFaProviderConfig  *(extends TwoFaProviderConfig, provider_type=`SMS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| verification_code_lifetime | int |  | [optional] |
| sms_verification_message_template | str |  |  |

#### TotpTwoFaProviderConfig  *(extends TwoFaProviderConfig, provider_type=`TOTP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| issuer_name | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.use_system_two_factor_auth_settings`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PlatformTwoFaSettings.model_validate(data)` or `PlatformTwoFaSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

