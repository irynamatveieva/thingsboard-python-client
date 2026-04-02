
# AccountTwoFaSettings

`tb_pe_client.models.AccountTwoFaSettings`

Account Two-Factor Authentication Settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **configs** | [**Dict[str, TwoFaAccountConfig]**](TwoFaAccountConfig.md) |  | [optional] |



## Referenced Types

#### TwoFaAccountConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| use_by_default | bool |  | [optional] |
| provider_type | str |  |  |

#### BackupCodeTwoFaAccountConfig  *(extends TwoFaAccountConfig, provider_type=`BACKUP_CODE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| codes | List[str] |  |  |
| codes_left | int |  | [optional] |

#### EmailTwoFaAccountConfig  *(extends TwoFaAccountConfig, provider_type=`EMAIL`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| email | str |  |  |

#### SmsTwoFaAccountConfig  *(extends TwoFaAccountConfig, provider_type=`SMS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| phone_number | str |  |  |

#### TotpTwoFaAccountConfig  *(extends TwoFaAccountConfig, provider_type=`TOTP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| auth_url | str |  |  |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.configs`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AccountTwoFaSettings.model_validate(data)` or `AccountTwoFaSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

