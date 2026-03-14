
# BackupCodeTwoFaAccountConfig

`tb_paas_client.models.BackupCodeTwoFaAccountConfig`

**Extends:** **TwoFaAccountConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **codes** | **List[str]** |  | |
| **codes_left** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.codes`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BackupCodeTwoFaAccountConfig.model_validate(data)` or `BackupCodeTwoFaAccountConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

