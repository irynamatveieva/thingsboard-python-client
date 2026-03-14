
# SnmpMapping

`tb_paas_client.models.SnmpMapping`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **oid** | **str** |  | [optional] |
| **key** | **str** |  | [optional] |
| **data_type** | [**DataType**](DataType.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.oid`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SnmpMapping.model_validate(data)` or `SnmpMapping.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

