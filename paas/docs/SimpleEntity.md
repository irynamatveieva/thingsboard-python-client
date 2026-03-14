
# SimpleEntity

`tb_paas_client.models.SimpleEntity`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **used** | **bool** |  | [optional] |
| **total_count** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.used`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SimpleEntity.model_validate(data)` or `SimpleEntity.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

