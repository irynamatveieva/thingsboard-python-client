
# JobResult

`tb_paas_client.models.JobResult`

Job execution result

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **successful_count** | **int** | Count of successfully completed tasks | [optional] |
| **failed_count** | **int** | Count of failed tasks | [optional] |
| **discarded_count** | **int** | Count of discarded tasks | [optional] |
| **total_count** | **int** | Total number of tasks, set when all tasks are submitted | [optional] |
| **results** | [**List[TaskResult]**](TaskResult.md) |  | [optional] |
| **general_error** | **str** | General error message if the job failed | [optional] |
| **start_ts** | **int** | Timestamp of the job start, in milliseconds | [optional] |
| **finish_ts** | **int** | Timestamp of the job finish, in milliseconds | [optional] |
| **cancellation_ts** | **int** | Timestamp of the job cancellation, in milliseconds | [optional] |
| **job_type** | **str** |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.successful_count`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `JobResult.model_validate(data)` or `JobResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

