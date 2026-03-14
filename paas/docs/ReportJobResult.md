
# ReportJobResult

`tb_paas_client.models.ReportJobResult`

**Extends:** **JobResult**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **report** | [**Report**](Report.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.report`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportJobResult.model_validate(data)` or `ReportJobResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

