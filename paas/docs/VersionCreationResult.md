
# VersionCreationResult

`tb_paas_client.models.VersionCreationResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version** | [**EntityVersion**](EntityVersion.md) |  | [optional] |
| **added** | **int** |  | [optional] |
| **modified** | **int** |  | [optional] |
| **removed** | **int** |  | [optional] |
| **error** | **str** |  | [optional] |
| **done** | **bool** |  | [optional] |



## Referenced Types

#### EntityVersion
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timestamp | int |  | [optional] |
| id | str |  | [optional] |
| name | str |  | [optional] |
| author | str |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.version`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionCreationResult.model_validate(data)` or `VersionCreationResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

