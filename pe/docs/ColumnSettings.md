
# ColumnSettings

`tb_pe_client.models.ColumnSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **column_width** | **str** |  | [optional] |
| **header** | [**CellSettings**](CellSettings.md) |  | [optional] |
| **cell** | [**CellSettings**](CellSettings.md) |  | [optional] |
| **type** | [**DataKeySettingsType**](DataKeySettingsType.md) | Data key settings type | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.column_width`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ColumnSettings.model_validate(data)` or `ColumnSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

