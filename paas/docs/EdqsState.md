
# EdqsState

`tb_paas_client.models.EdqsState`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **edqs_ready** | **bool** |  | [optional] |
| **sync_status** | [**EdqsSyncStatus**](EdqsSyncStatus.md) |  | [optional] |
| **api_mode** | [**EdqsApiMode**](EdqsApiMode.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.edqs_ready`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdqsState.model_validate(data)` or `EdqsState.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

