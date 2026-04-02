
# ErrorComponentAllOfExceptionCause

`tb_paas_client.models.ErrorComponentAllOfExceptionCause`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **stack_trace** | [**List[ErrorComponentAllOfExceptionCauseStackTrace]**](ErrorComponentAllOfExceptionCauseStackTrace.md) |  | [optional] |
| **message** | **str** |  | [optional] |
| **localized_message** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.stack_trace`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ErrorComponentAllOfExceptionCause.model_validate(data)` or `ErrorComponentAllOfExceptionCause.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

