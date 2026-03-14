
# EntityCountQuery

`tb_paas_client.models.EntityCountQuery`

A JSON value representing the entity count query. See API call notes above for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_filter** | [**EntityFilter**](EntityFilter.md) |  | [optional] |
| **key_filters** | [**List[KeyFilter]**](KeyFilter.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityCountQuery.model_validate(data)` or `EntityCountQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

