
# EntityDataQuery

`tb_ce_client.models.EntityDataQuery`

Entity data query to find entities. Page size is capped at 100.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_filter** | [**EntityFilter**](EntityFilter.md) |  | [optional] |
| **key_filters** | [**List[KeyFilter]**](KeyFilter.md) |  | [optional] |
| **page_link** | [**EntityDataPageLink**](EntityDataPageLink.md) |  | [optional] |
| **entity_fields** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **latest_values** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.entity_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataQuery.model_validate(data)` or `EntityDataQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

