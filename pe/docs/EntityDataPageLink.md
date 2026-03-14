
# EntityDataPageLink

`tb_pe_client.models.EntityDataPageLink`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **page_size** | **int** |  | [optional] |
| **page** | **int** |  | [optional] |
| **text_search** | **str** |  | [optional] |
| **sort_order** | [**EntityDataSortOrder**](EntityDataSortOrder.md) |  | [optional] |
| **dynamic** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.page_size`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataPageLink.model_validate(data)` or `EntityDataPageLink.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

