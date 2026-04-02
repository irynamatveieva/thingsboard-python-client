
# BackupCodeTwoFaProviderConfig

`tb_pe_client.models.BackupCodeTwoFaProviderConfig`

**Extends:** **TwoFaProviderConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **codes_quantity** | **int** |  | [optional] |



## Referenced Types

#### TwoFaProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_type | str |  |  |

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

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.codes_quantity`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BackupCodeTwoFaProviderConfig.model_validate(data)` or `BackupCodeTwoFaProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

