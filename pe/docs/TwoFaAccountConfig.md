
# TwoFaAccountConfig

`tb_pe_client.models.TwoFaAccountConfig`

Base configuration for two-factor authentication accounts

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **use_by_default** | **bool** |  | [optional] |
| **provider_type** | **str** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.use_by_default`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TwoFaAccountConfig.model_validate(data)` or `TwoFaAccountConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

