
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



## Referenced Types

#### SubmitStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | SubmitStrategyType |  | [optional] |
| batch_size | int |  | [optional] |

#### ProcessingStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ProcessingStrategyType |  | [optional] |
| retries | int |  | [optional] |
| failure_percentage | float |  | [optional] |
| pause_between_retries | int |  | [optional] |
| max_pause_between_retries | int |  | [optional] |

#### SubmitStrategyType (enum)
`BURST` | `BATCH` | `SEQUENTIAL_BY_ORIGINATOR` | `SEQUENTIAL_BY_TENANT` | `SEQUENTIAL`

#### ProcessingStrategyType (enum)
`SKIP_ALL_FAILURES` | `SKIP_ALL_FAILURES_AND_TIMED_OUT` | `RETRY_ALL` | `RETRY_FAILED` | `RETRY_TIMED_OUT` | `RETRY_FAILED_AND_TIMED_OUT`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantProfileQueueConfiguration.model_validate(data)` or `TenantProfileQueueConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

