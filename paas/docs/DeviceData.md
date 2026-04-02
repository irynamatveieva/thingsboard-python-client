
# DeviceData

`tb_paas_client.models.DeviceData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **configuration** | [**DeviceConfiguration**](DeviceConfiguration.md) | Device configuration for device profile type. DEFAULT is only supported value for now | [optional] |
| **transport_configuration** | [**DeviceTransportConfiguration**](DeviceTransportConfiguration.md) | Device transport configuration used to connect the device | [optional] |



## Referenced Types

#### DeviceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DeviceProfileType | Device profile type |  |

#### DefaultDeviceConfiguration  *(extends DeviceConfiguration, type=`DEFAULT`)*
*See DeviceConfiguration for properties.*

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

#### SnmpDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`SNMP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| host | str |  | [optional] |
| port | int |  | [optional] |
| protocol_version | SnmpProtocolVersion |  | [optional] |
| community | str |  | [optional] |
| username | str |  | [optional] |
| security_name | str |  | [optional] |
| context_name | str |  | [optional] |
| authentication_protocol | AuthenticationProtocol |  | [optional] |
| authentication_passphrase | str |  | [optional] |
| privacy_protocol | PrivacyProtocol |  | [optional] |
| privacy_passphrase | str |  | [optional] |
| engine_id | str |  | [optional] |

#### DeviceProfileType (enum)
`DEFAULT`

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

#### SnmpProtocolVersion (enum)
`V1` | `V2C` | `V3`

#### AuthenticationProtocol (enum)
`SHA_1` | `SHA_224` | `SHA_256` | `SHA_384` | `SHA_512` | `MD5`

#### PrivacyProtocol (enum)
`DES` | `AES_128` | `AES_192` | `AES_256`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceData.model_validate(data)` or `DeviceData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

