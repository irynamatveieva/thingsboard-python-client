
# TwilioSmsProviderConfiguration

`tb_pe_client.models.TwilioSmsProviderConfiguration`

**Extends:** **SmsProviderConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **account_sid** | **str** | Twilio account Sid. | [optional] |
| **account_token** | **str** | Twilio account Token. | [optional] |
| **number_from** | **str** | The number/id of a sender. | [optional] |



## Referenced Types

#### SmsProviderConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.account_sid`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TwilioSmsProviderConfiguration.model_validate(data)` or `TwilioSmsProviderConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

