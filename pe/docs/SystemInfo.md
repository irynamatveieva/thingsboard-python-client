
# SystemInfo

`tb_pe_client.models.SystemInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **monolith** | **bool** | Is monolith. | [optional] |
| **system_data** | [**List[SystemInfoData]**](SystemInfoData.md) | System data. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.monolith`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SystemInfo.model_validate(data)` or `SystemInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

