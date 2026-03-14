
# EntityRelationsQuery

`tb_paas_client.models.EntityRelationsQuery`

A JSON value representing the entity relations query object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **parameters** | [**RelationsSearchParameters**](RelationsSearchParameters.md) | Main search parameters. | [optional] |
| **filters** | [**List[RelationEntityTypeFilter]**](RelationEntityTypeFilter.md) | Main filters. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.parameters`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityRelationsQuery.model_validate(data)` or `EntityRelationsQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

