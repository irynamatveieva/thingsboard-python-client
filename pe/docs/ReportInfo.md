
# ReportInfo

`tb_pe_client.models.ReportInfo`

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
| **template_info** | [**EntityInfo**](EntityInfo.md) |  | [optional] |
| **customer_title** | **str** |  | [optional] |
| **user_name** | **str** |  | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportInfo.model_validate(data)` or `ReportInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

