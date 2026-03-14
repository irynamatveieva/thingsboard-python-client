
# VersionCreateConfig

`tb_paas_client.models.VersionCreateConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **save_relations** | **bool** |  | [optional] |
| **save_attributes** | **bool** |  | [optional] |
| **save_credentials** | **bool** |  | [optional] |
| **save_calculated_fields** | **bool** |  | [optional] |
| **save_permissions** | **bool** |  | [optional] |
| **save_group_entities** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.save_relations`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionCreateConfig.model_validate(data)` or `VersionCreateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

