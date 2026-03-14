
# EntityViewSearchQuery

`tb_pe_client.models.EntityViewSearchQuery`

The entity view search query JSON

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **parameters** | [**RelationsSearchParameters**](RelationsSearchParameters.md) | Main search parameters. | [optional] |
| **relation_type** | **str** | Type of the relation between root entity and device (e.g. 'Contains' or 'Manages'). | [optional] |
| **entity_view_types** | **List[str]** | Array of entity view types to filter the related entities (e.g. 'Temperature Sensor', 'Smoke Sensor'). | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.parameters`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityViewSearchQuery.model_validate(data)` or `EntityViewSearchQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

