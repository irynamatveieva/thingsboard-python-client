
# EntityDataDiff

`tb_paas_client.models.EntityDataDiff`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **current_version** | [**EntityExportData**](EntityExportData.md) |  | [optional] |
| **other_version** | [**EntityExportData**](EntityExportData.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.current_version`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataDiff.model_validate(data)` or `EntityDataDiff.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

