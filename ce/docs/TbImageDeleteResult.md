
# TbImageDeleteResult

`tb_ce_client.models.TbImageDeleteResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **success** | **bool** |  | [optional] |
| **references** | **Dict[str, List[HasIdObject]]** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.success`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbImageDeleteResult.model_validate(data)` or `TbImageDeleteResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

