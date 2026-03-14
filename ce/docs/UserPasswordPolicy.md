
# UserPasswordPolicy

`tb_ce_client.models.UserPasswordPolicy`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **minimum_length** | **int** | Minimum number of symbols in the password. | [optional] |
| **maximum_length** | **int** | Maximum number of symbols in the password. | [optional] |
| **minimum_uppercase_letters** | **int** | Minimum number of uppercase letters in the password. | [optional] |
| **minimum_lowercase_letters** | **int** | Minimum number of lowercase letters in the password. | [optional] |
| **minimum_digits** | **int** | Minimum number of digits in the password. | [optional] |
| **minimum_special_characters** | **int** | Minimum number of special in the password. | [optional] |
| **allow_whitespaces** | **bool** | Allow whitespaces | [optional] |
| **force_user_to_reset_password_if_not_valid** | **bool** | Force user to update password if existing one does not pass validation | [optional] |
| **password_expiration_period_days** | **int** | Password expiration period (days). Force expiration of the password. | [optional] |
| **password_reuse_frequency_days** | **int** | Password reuse frequency (days). Disallow to use the same password for the defined number of days | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.minimum_length`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserPasswordPolicy.model_validate(data)` or `UserPasswordPolicy.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

