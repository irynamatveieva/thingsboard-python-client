
# ProcessingStrategy

`tb_pe_client.models.ProcessingStrategy`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**ProcessingStrategyType**](ProcessingStrategyType.md) |  | [optional] |
| **retries** | **int** |  | [optional] |
| **failure_percentage** | **float** |  | [optional] |
| **pause_between_retries** | **int** |  | [optional] |
| **max_pause_between_retries** | **int** |  | [optional] |



## Referenced Types

#### ProcessingStrategyType (enum)
`SKIP_ALL_FAILURES` | `SKIP_ALL_FAILURES_AND_TIMED_OUT` | `RETRY_ALL` | `RETRY_FAILED` | `RETRY_TIMED_OUT` | `RETRY_FAILED_AND_TIMED_OUT`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ProcessingStrategy.model_validate(data)` or `ProcessingStrategy.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

