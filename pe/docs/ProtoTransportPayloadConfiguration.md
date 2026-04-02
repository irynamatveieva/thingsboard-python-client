
# ProtoTransportPayloadConfiguration

`tb_pe_client.models.ProtoTransportPayloadConfiguration`

**Extends:** **TransportPayloadTypeConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **device_telemetry_proto_schema** | **str** |  | [optional] |
| **device_attributes_proto_schema** | **str** |  | [optional] |
| **device_rpc_request_proto_schema** | **str** |  | [optional] |
| **device_rpc_response_proto_schema** | **str** |  | [optional] |
| **enable_compatibility_with_json_payload_format** | **bool** |  | [optional] |
| **use_json_payload_format_for_default_downlink_topics** | **bool** |  | [optional] |



## Referenced Types

#### TransportPayloadTypeConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| transport_payload_type | str |  |  |

#### JsonTransportPayloadConfiguration  *(extends TransportPayloadTypeConfiguration, transport_payload_type=`JSON`)*
*See TransportPayloadTypeConfiguration for properties.*

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.device_telemetry_proto_schema`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ProtoTransportPayloadConfiguration.model_validate(data)` or `ProtoTransportPayloadConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

