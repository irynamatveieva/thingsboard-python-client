
# MqttDeviceProfileTransportConfiguration

`tb_paas_client.models.MqttDeviceProfileTransportConfiguration`

**Extends:** **DeviceProfileTransportConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **device_telemetry_topic** | **str** |  | [optional] |
| **device_attributes_topic** | **str** |  | [optional] |
| **device_attributes_subscribe_topic** | **str** |  | [optional] |
| **transport_payload_type_configuration** | [**TransportPayloadTypeConfiguration**](TransportPayloadTypeConfiguration.md) |  | [optional] |
| **sparkplug** | **bool** |  | [optional] |
| **sparkplug_attributes_metric_names** | **List[str]** |  | [optional] |
| **send_ack_on_validation_exception** | **bool** |  | [optional] |



## Referenced Types

#### DeviceProfileTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TransportPayloadTypeConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| transport_payload_type | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.device_telemetry_topic`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MqttDeviceProfileTransportConfiguration.model_validate(data)` or `MqttDeviceProfileTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

