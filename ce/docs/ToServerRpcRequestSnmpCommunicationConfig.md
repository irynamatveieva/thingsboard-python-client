
# ToServerRpcRequestSnmpCommunicationConfig

`tb_ce_client.models.ToServerRpcRequestSnmpCommunicationConfig`

**Extends:** **SnmpCommunicationConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **mappings** | [**List[SnmpMapping]**](SnmpMapping.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.mappings`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ToServerRpcRequestSnmpCommunicationConfig.model_validate(data)` or `ToServerRpcRequestSnmpCommunicationConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

