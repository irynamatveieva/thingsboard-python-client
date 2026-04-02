
# TenantProfile

`tb_paas_client.models.TenantProfile`

A JSON value representing the tenant profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**TenantProfileId**](TenantProfileId.md) | JSON object with the tenant profile Id. Specify this field to update the tenant profile. Referencing non-existing tenant profile Id will cause error. Omit this field to create new tenant profile. | [optional] |
| **created_time** | **int** | Timestamp of the tenant profile creation, in milliseconds | [optional] [readonly] |
| **name** | **str** | Name of the tenant profile | [optional] |
| **description** | **str** | Description of the tenant profile | [optional] |
| **default** | **bool** | Default Tenant profile to be used. | [optional] |
| **isolated_tb_rule_engine** | **bool** | If enabled, will push all messages related to this tenant and processed by the rule engine into separate queue. Useful for complex microservices deployments, to isolate processing of the data for specific tenants | [optional] |
| **profile_data** | [**TenantProfileData**](TenantProfileData.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`TenantProfileId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### TenantProfileData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| configuration | TenantProfileConfiguration | Complex JSON object that contains profile settings: max devices, max assets, rate limits, etc. | [optional] |
| queue_configuration | List[TenantProfileQueueConfiguration] | JSON array of queue configuration per tenant profile | [optional] |

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

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

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
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantProfile.model_validate(data)` or `TenantProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

