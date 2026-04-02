
# Job

`tb_paas_client.models.Job`

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



## Referenced Types

> **EntityId types** (`JobId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### JobType (enum)
`CF_REPROCESSING` | `REPORT` | `DUMMY`

#### JobStatus (enum)
`QUEUED` | `PENDING` | `RUNNING` | `COMPLETED` | `FAILED` | `CANCELLED`

#### JobConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tasks_key | str |  |  |
| to_reprocess | List[TaskResult] |  | [optional] |
| type | str |  |  |

#### JobResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| successful_count | int | Count of successfully completed tasks | [optional] |
| failed_count | int | Count of failed tasks | [optional] |
| discarded_count | int | Count of discarded tasks | [optional] |
| total_count | int | Total number of tasks, set when all tasks are submitted | [optional] |
| results | List[TaskResult] |  | [optional] |
| general_error | str | General error message if the job failed | [optional] |
| start_ts | int | Timestamp of the job start, in milliseconds | [optional] |
| finish_ts | int | Timestamp of the job finish, in milliseconds | [optional] |
| cancellation_ts | int | Timestamp of the job cancellation, in milliseconds | [optional] |
| job_type | str |  |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### TaskResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| success | bool |  | [optional] |
| discarded | bool |  | [optional] |
| finish_ts | int |  | [optional] |
| job_type | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Job.model_validate(data)` or `Job.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

