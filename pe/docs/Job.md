
# Job

`tb_pe_client.models.Job`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**JobId**](JobId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | |
| **type** | [**JobType**](JobType.md) |  | |
| **key** | **str** |  | |
| **entity_id** | [**EntityId**](EntityId.md) |  | |
| **entity_name** | **str** |  | [optional] |
| **status** | [**JobStatus**](JobStatus.md) |  | |
| **configuration** | [**JobConfiguration**](JobConfiguration.md) |  | |
| **result** | [**JobResult**](JobResult.md) |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Job.model_validate(data)` or `Job.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

