
# TbResourceDeleteResult

`tb_ce_client.models.TbResourceDeleteResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **success** | **bool** |  | [optional] |
| **references** | **Dict[str, List[EntityInfo]]** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.success`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbResourceDeleteResult.model_validate(data)` or `TbResourceDeleteResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

