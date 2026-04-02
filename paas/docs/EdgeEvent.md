
# EdgeEvent

`tb_paas_client.models.EdgeEvent`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EdgeEventId**](EdgeEventId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **seq_id** | **int** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **edge_id** | [**EdgeId**](EdgeId.md) |  | [optional] |
| **action** | [**EdgeEventActionType**](EdgeEventActionType.md) |  | [optional] |
| **entity_id** | **UUID** |  | [optional] |
| **uid** | **str** |  | [optional] |
| **type** | [**EdgeEventType**](EdgeEventType.md) |  | [optional] |
| **body** | **object** |  | [optional] |
| **entity_group_id** | **UUID** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeEvent.model_validate(data)` or `EdgeEvent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

