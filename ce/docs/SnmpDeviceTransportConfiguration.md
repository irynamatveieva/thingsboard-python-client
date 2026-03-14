
# SnmpDeviceTransportConfiguration

`tb_ce_client.models.SnmpDeviceTransportConfiguration`

**Extends:** **DeviceTransportConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **host** | **str** |  | [optional] |
| **port** | **int** |  | [optional] |
| **protocol_version** | [**SnmpProtocolVersion**](SnmpProtocolVersion.md) |  | [optional] |
| **community** | **str** |  | [optional] |
| **username** | **str** |  | [optional] |
| **security_name** | **str** |  | [optional] |
| **context_name** | **str** |  | [optional] |
| **authentication_protocol** | [**AuthenticationProtocol**](AuthenticationProtocol.md) |  | [optional] |
| **authentication_passphrase** | **str** |  | [optional] |
| **privacy_protocol** | [**PrivacyProtocol**](PrivacyProtocol.md) |  | [optional] |
| **privacy_passphrase** | **str** |  | [optional] |
| **engine_id** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.host`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SnmpDeviceTransportConfiguration.model_validate(data)` or `SnmpDeviceTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

