
# EntityRelation

`tb_paas_client.models.EntityRelation`

A JSON value representing the relation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **var_from** | [**EntityId**](EntityId.md) | JSON object with [from] Entity Id. | |
| **to** | [**EntityId**](EntityId.md) | JSON object with [to] Entity Id. | |
| **type** | **str** | String value of relation type. | |
| **type_group** | [**RelationTypeGroup**](RelationTypeGroup.md) | Represents the type group of the relation. | |
| **version** | **int** |  | [optional] |
| **additional_info** | **object** | Additional parameters of the relation. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.var_from`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityRelation.model_validate(data)` or `EntityRelation.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

