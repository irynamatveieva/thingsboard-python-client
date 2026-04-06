
# TelemetryQueryingSnmpCommunicationConfig

`tb_ce_client.models.TelemetryQueryingSnmpCommunicationConfig`

**Extends:** **SnmpCommunicationConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **mappings** | [**List[SnmpMapping]**](SnmpMapping.md) |  | [optional] |
| **querying_frequency_ms** | **int** |  | [optional] |



## Referenced Types

#### SnmpCommunicationConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| spec | SnmpCommunicationSpec | Specification of the SNMP communication |  |

#### SnmpMapping
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| oid | str |  | [optional] |
| key | str |  | [optional] |
| data_type | DataType |  | [optional] |

#### SnmpCommunicationSpec (enum)
`TELEMETRY_QUERYING` | `CLIENT_ATTRIBUTES_QUERYING` | `SHARED_ATTRIBUTES_SETTING` | `TO_DEVICE_RPC_REQUEST` | `TO_SERVER_RPC_REQUEST`

#### DataType (enum)
`BOOLEAN` | `LONG` | `DOUBLE` | `STRING` | `JSON`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.mappings`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TelemetryQueryingSnmpCommunicationConfig.model_validate(data)` or `TelemetryQueryingSnmpCommunicationConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

