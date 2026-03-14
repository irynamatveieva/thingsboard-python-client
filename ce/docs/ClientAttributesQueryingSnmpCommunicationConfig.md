
# ClientAttributesQueryingSnmpCommunicationConfig

`tb_ce_client.models.ClientAttributesQueryingSnmpCommunicationConfig`

**Extends:** **SnmpCommunicationConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **mappings** | [**List[SnmpMapping]**](SnmpMapping.md) |  | [optional] |
| **querying_frequency_ms** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.mappings`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ClientAttributesQueryingSnmpCommunicationConfig.model_validate(data)` or `ClientAttributesQueryingSnmpCommunicationConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

