
# SecuritySettings

`tb_pe_client.models.SecuritySettings`

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



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.password_policy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SecuritySettings.model_validate(data)` or `SecuritySettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

