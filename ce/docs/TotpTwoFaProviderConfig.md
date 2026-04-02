
# TotpTwoFaProviderConfig

`tb_ce_client.models.TotpTwoFaProviderConfig`

**Extends:** **TwoFaProviderConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **issuer_name** | **str** |  | |



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

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.issuer_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TotpTwoFaProviderConfig.model_validate(data)` or `TotpTwoFaProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

