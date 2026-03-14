
# CfReprocessingTaskResult

`tb_pe_client.models.CfReprocessingTaskResult`

**Extends:** **TaskResult**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **failure** | [**CfReprocessingTaskFailure**](CfReprocessingTaskFailure.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.failure`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CfReprocessingTaskResult.model_validate(data)` or `CfReprocessingTaskResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

