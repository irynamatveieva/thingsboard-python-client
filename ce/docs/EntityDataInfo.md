
# EntityDataInfo

`tb_ce_client.models.EntityDataInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **has_relations** | **bool** |  | [optional] |
| **has_attributes** | **bool** |  | [optional] |
| **has_credentials** | **bool** |  | [optional] |
| **has_calculated_fields** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.has_relations`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataInfo.model_validate(data)` or `EntityDataInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

