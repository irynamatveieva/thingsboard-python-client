
# SnmpCommunicationConfig

`tb_pe_client.models.SnmpCommunicationConfig`

SNMP communication configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **spec** | [**SnmpCommunicationSpec**](SnmpCommunicationSpec.md) | Specification of the SNMP communication | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.spec`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SnmpCommunicationConfig.model_validate(data)` or `SnmpCommunicationConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

