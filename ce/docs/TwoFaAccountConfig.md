
# TwoFaAccountConfig

`tb_ce_client.models.TwoFaAccountConfig`

Base configuration for two-factor authentication accounts

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **use_by_default** | **bool** |  | [optional] |
| **provider_type** | **str** |  | |



## Subtypes

#### BackupCodeTwoFaAccountConfig  *(provider_type=`BACKUP_CODE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| codes | List[str] |  |  |
| codes_left | int |  | [optional] |

#### EmailTwoFaAccountConfig  *(provider_type=`EMAIL`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| email | str |  |  |

#### SmsTwoFaAccountConfig  *(provider_type=`SMS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| phone_number | str |  |  |

#### TotpTwoFaAccountConfig  *(provider_type=`TOTP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| auth_url | str |  |  |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.use_by_default`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TwoFaAccountConfig.model_validate(data)` or `TwoFaAccountConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

