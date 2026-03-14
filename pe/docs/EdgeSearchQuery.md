
# EdgeSearchQuery

`tb_pe_client.models.EdgeSearchQuery`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **parameters** | [**RelationsSearchParameters**](RelationsSearchParameters.md) | Main search parameters. | [optional] |
| **relation_type** | **str** | Type of the relation between root entity and edge (e.g. 'Contains' or 'Manages'). | [optional] |
| **edge_types** | **List[str]** | Array of edge types to filter the related entities (e.g. 'Silos', 'Stores'). | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.parameters`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeSearchQuery.model_validate(data)` or `EdgeSearchQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

