
# Queue

`tb_pe_client.models.Queue`

A JSON value representing the queue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**QueueId**](QueueId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **additional_info** | **object** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **name** | **str** |  | [optional] |
| **topic** | **str** |  | [optional] |
| **poll_interval** | **int** |  | [optional] |
| **partitions** | **int** |  | [optional] |
| **consumer_per_partition** | **bool** |  | [optional] |
| **pack_processing_timeout** | **int** |  | [optional] |
| **submit_strategy** | [**SubmitStrategy**](SubmitStrategy.md) |  | [optional] |
| **processing_strategy** | [**ProcessingStrategy**](ProcessingStrategy.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Queue.model_validate(data)` or `Queue.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

