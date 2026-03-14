
# EdgeTypeFilter

`tb_pe_client.models.EdgeTypeFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **edge_types** | **List[str]** |  | [optional] |
| **edge_name_filter** | **str** |  | [optional] |
| **edge_type** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.edge_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeTypeFilter.model_validate(data)` or `EdgeTypeFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

