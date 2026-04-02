
# ReadTsKvQueryResult

`tb_pe_client.models.ReadTsKvQueryResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **query_id** | **int** |  | [optional] |
| **data** | [**List[TsKvEntry]**](TsKvEntry.md) |  | [optional] |
| **last_entry_ts** | **int** |  | [optional] |



## Referenced Types

#### TsKvEntry
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ts | int |  | [optional] |
| value | object |  | [optional] |
| key | str |  | [optional] |
| double_value | float |  | [optional] |
| long_value | int |  | [optional] |
| boolean_value | bool |  | [optional] |
| value_as_string | str |  | [optional] |
| data_type | DataType |  | [optional] |
| json_value | str |  | [optional] |
| str_value | str |  | [optional] |
| version | int |  | [optional] |

#### DataType (enum)
`BOOLEAN` | `LONG` | `DOUBLE` | `STRING` | `JSON`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.query_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReadTsKvQueryResult.model_validate(data)` or `ReadTsKvQueryResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

