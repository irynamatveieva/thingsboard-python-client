
# ProtoTransportPayloadConfiguration

`tb_ce_client.models.ProtoTransportPayloadConfiguration`

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



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.device_telemetry_proto_schema`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ProtoTransportPayloadConfiguration.model_validate(data)` or `ProtoTransportPayloadConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

