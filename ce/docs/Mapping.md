
# Mapping

`tb_ce_client.models.Mapping`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **columns** | [**List[ColumnMapping]**](ColumnMapping.md) |  | [optional] |
| **delimiter** | **str** |  | [optional] |
| **update** | **bool** |  | [optional] |
| **header** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.columns`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Mapping.model_validate(data)` or `Mapping.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

