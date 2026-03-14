
# DebugSettings

`tb_pe_client.models.DebugSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **failures_enabled** | **bool** | Debug failures.  | [optional] |
| **all_enabled** | **bool** | Debug All. Used as a trigger for updating debugAllUntil. | [optional] |
| **all_enabled_until** | **int** | Timestamp of the end time for the processing debug events. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.failures_enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DebugSettings.model_validate(data)` or `DebugSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

