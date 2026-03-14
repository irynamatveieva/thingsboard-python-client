
# ReportTaskResult

`tb_paas_client.models.ReportTaskResult`

**Extends:** **TaskResult**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **report** | [**Report**](Report.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.report`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportTaskResult.model_validate(data)` or `ReportTaskResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

