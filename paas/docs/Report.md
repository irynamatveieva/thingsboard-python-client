
# Report

`tb_paas_client.models.Report`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**ReportId**](ReportId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | |
| **customer_id** | [**CustomerId**](CustomerId.md) |  | [optional] |
| **template_id** | [**ReportTemplateId**](ReportTemplateId.md) |  | |
| **format** | [**TbReportFormat**](TbReportFormat.md) |  | |
| **name** | **str** |  | |
| **user_id** | [**UserId**](UserId.md) |  | |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Report.model_validate(data)` or `Report.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

