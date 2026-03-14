
# ReadTsKvQueryResult

`tb_paas_client.models.ReadTsKvQueryResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **query_id** | **int** |  | [optional] |
| **data** | [**List[TsKvEntry]**](TsKvEntry.md) |  | [optional] |
| **last_entry_ts** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.query_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReadTsKvQueryResult.model_validate(data)` or `ReadTsKvQueryResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

