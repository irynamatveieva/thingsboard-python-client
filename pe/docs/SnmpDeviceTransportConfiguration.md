
# SnmpDeviceTransportConfiguration

`tb_pe_client.models.SnmpDeviceTransportConfiguration`

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



## Referenced Types

#### DeviceTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CoapDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`COAP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| power_mode | PowerMode |  | [optional] |
| psm_activity_timer | int |  | [optional] |
| edrx_cycle | int |  | [optional] |
| paging_transmission_window | int |  | [optional] |

#### DefaultDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`DEFAULT`)*
*See DeviceTransportConfiguration for properties.*

#### Lwm2mDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`LWM2M`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| power_mode | PowerMode |  | [optional] |
| psm_activity_timer | int |  | [optional] |
| edrx_cycle | int |  | [optional] |
| paging_transmission_window | int |  | [optional] |

#### MqttDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`MQTT`)*
*See DeviceTransportConfiguration for properties.*

#### SnmpProtocolVersion (enum)
`V1` | `V2C` | `V3`

#### AuthenticationProtocol (enum)
`SHA_1` | `SHA_224` | `SHA_256` | `SHA_384` | `SHA_512` | `MD5`

#### PrivacyProtocol (enum)
`DES` | `AES_128` | `AES_192` | `AES_256`

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.host`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SnmpDeviceTransportConfiguration.model_validate(data)` or `SnmpDeviceTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

