
# TwoFaProviderInfo

`tb_pe_client.models.TwoFaProviderInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**TwoFaProviderType**](TwoFaProviderType.md) |  | [optional] |
| **default** | **bool** |  | [optional] |
| **contact** | **str** |  | [optional] |
| **min_verification_code_send_period** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TwoFaProviderInfo.model_validate(data)` or `TwoFaProviderInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

