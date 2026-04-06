
# DefaultCoapDeviceTypeConfiguration

`tb_ce_client.models.DefaultCoapDeviceTypeConfiguration`

**Extends:** **CoapDeviceTypeConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **transport_payload_type_configuration** | [**TransportPayloadTypeConfiguration**](TransportPayloadTypeConfiguration.md) |  | [optional] |



## Referenced Types

#### CoapDeviceTypeConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| coap_device_type | str |  |  |

#### TransportPayloadTypeConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| transport_payload_type | str |  |  |

#### JsonTransportPayloadConfiguration  *(extends TransportPayloadTypeConfiguration, transport_payload_type=`JSON`)*
*See TransportPayloadTypeConfiguration for properties.*

#### ProtoTransportPayloadConfiguration  *(extends TransportPayloadTypeConfiguration, transport_payload_type=`PROTOBUF`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| device_telemetry_proto_schema | str |  | [optional] |
| device_attributes_proto_schema | str |  | [optional] |
| device_rpc_request_proto_schema | str |  | [optional] |
| device_rpc_response_proto_schema | str |  | [optional] |
| enable_compatibility_with_json_payload_format | bool |  | [optional] |
| use_json_payload_format_for_default_downlink_topics | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.transport_payload_type_configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DefaultCoapDeviceTypeConfiguration.model_validate(data)` or `DefaultCoapDeviceTypeConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

