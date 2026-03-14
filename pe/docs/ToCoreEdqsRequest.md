
# ToCoreEdqsRequest

`tb_pe_client.models.ToCoreEdqsRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sync_request** | [**EdqsSyncRequest**](EdqsSyncRequest.md) |  | [optional] |
| **api_enabled** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.sync_request`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ToCoreEdqsRequest.model_validate(data)` or `ToCoreEdqsRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

