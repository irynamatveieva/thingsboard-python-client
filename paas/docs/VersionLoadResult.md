
# VersionLoadResult

`tb_paas_client.models.VersionLoadResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **result** | [**List[EntityTypeLoadResult]**](EntityTypeLoadResult.md) |  | [optional] |
| **error** | [**EntityLoadError**](EntityLoadError.md) |  | [optional] |
| **done** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.result`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionLoadResult.model_validate(data)` or `VersionLoadResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

