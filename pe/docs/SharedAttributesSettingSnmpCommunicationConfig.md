
# SharedAttributesSettingSnmpCommunicationConfig

`tb_pe_client.models.SharedAttributesSettingSnmpCommunicationConfig`

**Extends:** **SnmpCommunicationConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **mappings** | [**List[SnmpMapping]**](SnmpMapping.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.mappings`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SharedAttributesSettingSnmpCommunicationConfig.model_validate(data)` or `SharedAttributesSettingSnmpCommunicationConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

