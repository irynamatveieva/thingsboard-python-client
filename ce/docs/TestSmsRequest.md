
# TestSmsRequest

`tb_ce_client.models.TestSmsRequest`

A JSON value representing the Test SMS request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider_configuration** | [**SmsProviderConfiguration**](SmsProviderConfiguration.md) | The SMS provider configuration | [optional] |
| **number_to** | **str** | The phone number or other identifier to specify as a recipient of the SMS. | [optional] |
| **message** | **str** | The test message | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.provider_configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TestSmsRequest.model_validate(data)` or `TestSmsRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

