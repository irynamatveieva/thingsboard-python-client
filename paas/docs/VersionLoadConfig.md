
# VersionLoadConfig

`tb_paas_client.models.VersionLoadConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **load_relations** | **bool** |  | [optional] |
| **load_attributes** | **bool** |  | [optional] |
| **load_credentials** | **bool** |  | [optional] |
| **load_calculated_fields** | **bool** |  | [optional] |
| **load_permissions** | **bool** |  | [optional] |
| **load_group_entities** | **bool** |  | [optional] |
| **auto_generate_integration_key** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.load_relations`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionLoadConfig.model_validate(data)` or `VersionLoadConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

