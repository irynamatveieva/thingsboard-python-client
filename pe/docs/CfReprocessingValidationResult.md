
# CfReprocessingValidationResult

`tb_pe_client.models.CfReprocessingValidationResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **is_valid** | **bool** |  | [optional] |
| **message** | **str** |  | [optional] |
| **last_job_status** | [**JobStatus**](JobStatus.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.is_valid`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CfReprocessingValidationResult.model_validate(data)` or `CfReprocessingValidationResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

