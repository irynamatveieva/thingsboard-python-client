
# SecuritySettings

`tb_ce_client.models.SecuritySettings`

A JSON value representing the Security Settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **password_policy** | [**UserPasswordPolicy**](UserPasswordPolicy.md) | The user password policy object. | [optional] |
| **max_failed_login_attempts** | **int** | Maximum number of failed login attempts allowed before user account is locked. | [optional] |
| **user_lockout_notification_email** | **str** | Email to use for notifications about locked users. | [optional] |
| **mobile_secret_key_length** | **int** | Mobile secret key length | [optional] |
| **user_activation_token_ttl** | **int** | TTL in hours for user activation link | |
| **password_reset_token_ttl** | **int** | TTL in hours for password reset link | |



## Referenced Types

#### UserPasswordPolicy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| minimum_length | int | Minimum number of symbols in the password. | [optional] |
| maximum_length | int | Maximum number of symbols in the password. | [optional] |
| minimum_uppercase_letters | int | Minimum number of uppercase letters in the password. | [optional] |
| minimum_lowercase_letters | int | Minimum number of lowercase letters in the password. | [optional] |
| minimum_digits | int | Minimum number of digits in the password. | [optional] |
| minimum_special_characters | int | Minimum number of special in the password. | [optional] |
| allow_whitespaces | bool | Allow whitespaces | [optional] |
| force_user_to_reset_password_if_not_valid | bool | Force user to update password if existing one does not pass validation | [optional] |
| password_expiration_period_days | int | Password expiration period (days). Force expiration of the password. | [optional] |
| password_reuse_frequency_days | int | Password reuse frequency (days). Disallow to use the same password for the defined number of days | [optional] |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.password_policy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SecuritySettings.model_validate(data)` or `SecuritySettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

