
# BulkImportRequest

`tb_pe_client.models.BulkImportRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **file** | **str** |  | [optional] |
| **mapping** | [**Mapping**](Mapping.md) |  | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) |  | [optional] |
| **entity_group_id** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.file`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BulkImportRequest.model_validate(data)` or `BulkImportRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

