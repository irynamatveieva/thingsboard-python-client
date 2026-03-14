
# BulkImportResultAsset

`tb_pe_client.models.BulkImportResultAsset`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **created** | **int** |  | [optional] |
| **updated** | **int** |  | [optional] |
| **errors** | **int** |  | [optional] |
| **errors_list** | **List[str]** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.created`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BulkImportResultAsset.model_validate(data)` or `BulkImportResultAsset.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

