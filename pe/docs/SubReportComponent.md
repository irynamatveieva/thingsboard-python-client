
# SubReportComponent

`tb_pe_client.models.SubReportComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data_sources** | [**List[DataSource]**](DataSource.md) |  | [optional] |
| **template_id** | [**ReportTemplateId**](ReportTemplateId.md) |  | [optional] |
| **avoid_page_break_inside** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data_sources`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SubReportComponent.model_validate(data)` or `SubReportComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

