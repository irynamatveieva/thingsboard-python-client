
# TotpTwoFaProviderConfig

`tb_paas_client.models.TotpTwoFaProviderConfig`

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

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.issuer_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TotpTwoFaProviderConfig.model_validate(data)` or `TotpTwoFaProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

