
# EntityRelationInfo

`tb_pe_client.models.EntityRelationInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **var_from** | [**EntityId**](EntityId.md) | JSON object with [from] Entity Id. | |
| **to** | [**EntityId**](EntityId.md) | JSON object with [to] Entity Id. | |
| **type** | **str** | String value of relation type. | |
| **type_group** | [**RelationTypeGroup**](RelationTypeGroup.md) | Represents the type group of the relation. | |
| **version** | **int** |  | [optional] |
| **from_name** | **str** | Name of the entity for [from] direction. | [optional] [readonly] |
| **to_name** | **str** | Name of the entity for [to] direction. | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the relation. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.var_from`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityRelationInfo.model_validate(data)` or `EntityRelationInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

