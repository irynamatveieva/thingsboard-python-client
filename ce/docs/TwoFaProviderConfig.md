
# TwoFaProviderConfig

`tb_ce_client.models.TwoFaProviderConfig`

Two-factor authentication provider configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider_type** | **str** |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.provider_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TwoFaProviderConfig.model_validate(data)` or `TwoFaProviderConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

