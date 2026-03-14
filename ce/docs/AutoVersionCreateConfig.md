
# AutoVersionCreateConfig

`tb_ce_client.models.AutoVersionCreateConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **save_relations** | **bool** |  | [optional] |
| **save_attributes** | **bool** |  | [optional] |
| **save_credentials** | **bool** |  | [optional] |
| **save_calculated_fields** | **bool** |  | [optional] |
| **branch** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.save_relations`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AutoVersionCreateConfig.model_validate(data)` or `AutoVersionCreateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

