
# AccountTwoFaSettings

`tb_ce_client.models.AccountTwoFaSettings`

Account Two-Factor Authentication Settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **configs** | [**Dict[str, TwoFaAccountConfig]**](TwoFaAccountConfig.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.configs`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AccountTwoFaSettings.model_validate(data)` or `AccountTwoFaSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

