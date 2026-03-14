
# Entity

`tb_pe_client.models.Entity`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **used** | **bool** |  | [optional] |
| **active_count** | **int** |  | [optional] |
| **total_count** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.used`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Entity.model_validate(data)` or `Entity.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

