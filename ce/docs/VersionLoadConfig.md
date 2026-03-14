
# VersionLoadConfig

`tb_ce_client.models.VersionLoadConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **load_relations** | **bool** |  | [optional] |
| **load_attributes** | **bool** |  | [optional] |
| **load_credentials** | **bool** |  | [optional] |
| **load_calculated_fields** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.load_relations`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionLoadConfig.model_validate(data)` or `VersionLoadConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

