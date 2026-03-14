
# EventInfo

`tb_ce_client.models.EventInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EventId**](EventId.md) |  | [optional] |
| **created_time** | **int** | Timestamp of the event creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **type** | **str** | Event type | [optional] |
| **uid** | **str** | string | [optional] |
| **entity_id** | [**EntityId**](EntityId.md) | JSON object with Entity Id for which event is created. | [optional] [readonly] |
| **body** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EventInfo.model_validate(data)` or `EventInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

