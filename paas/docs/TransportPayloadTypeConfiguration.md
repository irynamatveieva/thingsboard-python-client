
# TransportPayloadTypeConfiguration

`tb_paas_client.models.TransportPayloadTypeConfiguration`

Configuration for transport payload type

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **transport_payload_type** | **str** |  | |



## Subtypes

#### JsonTransportPayloadConfiguration  *(transport_payload_type=`JSON`)*
*(no additional properties)*

#### ProtoTransportPayloadConfiguration  *(transport_payload_type=`PROTOBUF`)*
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

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.transport_payload_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TransportPayloadTypeConfiguration.model_validate(data)` or `TransportPayloadTypeConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

