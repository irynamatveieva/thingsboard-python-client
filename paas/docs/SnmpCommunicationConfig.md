
# SnmpCommunicationConfig

`tb_paas_client.models.SnmpCommunicationConfig`

SNMP communication configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **spec** | [**SnmpCommunicationSpec**](SnmpCommunicationSpec.md) | Specification of the SNMP communication | |



## Referenced Types

#### SnmpCommunicationSpec (enum)
`TELEMETRY_QUERYING` | `CLIENT_ATTRIBUTES_QUERYING` | `SHARED_ATTRIBUTES_SETTING` | `TO_DEVICE_RPC_REQUEST` | `TO_SERVER_RPC_REQUEST`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.spec`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SnmpCommunicationConfig.model_validate(data)` or `SnmpCommunicationConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

