
# TenantProfileData

`tb_paas_client.models.TenantProfileData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **configuration** | [**TenantProfileConfiguration**](TenantProfileConfiguration.md) | Complex JSON object that contains profile settings: max devices, max assets, rate limits, etc. | [optional] |
| **queue_configuration** | [**List[TenantProfileQueueConfiguration]**](TenantProfileQueueConfiguration.md) | JSON array of queue configuration per tenant profile | [optional] |



## Referenced Types

#### TenantProfileConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TenantProfileQueueConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str |  | [optional] |
| topic | str |  | [optional] |
| poll_interval | int |  | [optional] |
| partitions | int |  | [optional] |
| consumer_per_partition | bool |  | [optional] |
| pack_processing_timeout | int |  | [optional] |
| submit_strategy | SubmitStrategy |  | [optional] |
| processing_strategy | ProcessingStrategy |  | [optional] |
| additional_info | object |  | [optional] |

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

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantProfileData.model_validate(data)` or `TenantProfileData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

