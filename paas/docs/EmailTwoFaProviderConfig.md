
# EmailTwoFaProviderConfig

`tb_paas_client.models.EmailTwoFaProviderConfig`

**Extends:** **TwoFaProviderConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **verification_code_lifetime** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.verification_code_lifetime`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EmailTwoFaProviderConfig.model_validate(data)` or `EmailTwoFaProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

