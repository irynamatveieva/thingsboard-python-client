
# TenantProfileQueueConfiguration

`tb_pe_client.models.TenantProfileQueueConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name** | **str** |  | [optional] |
| **topic** | **str** |  | [optional] |
| **poll_interval** | **int** |  | [optional] |
| **partitions** | **int** |  | [optional] |
| **consumer_per_partition** | **bool** |  | [optional] |
| **pack_processing_timeout** | **int** |  | [optional] |
| **submit_strategy** | [**SubmitStrategy**](SubmitStrategy.md) |  | [optional] |
| **processing_strategy** | [**ProcessingStrategy**](ProcessingStrategy.md) |  | [optional] |
| **additional_info** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantProfileQueueConfiguration.model_validate(data)` or `TenantProfileQueueConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

