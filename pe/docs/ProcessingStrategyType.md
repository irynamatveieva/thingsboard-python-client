
# ProcessingStrategyType

`tb_pe_client.models.ProcessingStrategyType`

## Enum Values


* `SKIP_ALL_FAILURES` (value: `'SKIP_ALL_FAILURES'`)

* `SKIP_ALL_FAILURES_AND_TIMED_OUT` (value: `'SKIP_ALL_FAILURES_AND_TIMED_OUT'`)

* `RETRY_ALL` (value: `'RETRY_ALL'`)

* `RETRY_FAILED` (value: `'RETRY_FAILED'`)

* `RETRY_TIMED_OUT` (value: `'RETRY_TIMED_OUT'`)

* `RETRY_FAILED_AND_TIMED_OUT` (value: `'RETRY_FAILED_AND_TIMED_OUT'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ProcessingStrategyType.model_validate(data)` or `ProcessingStrategyType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

