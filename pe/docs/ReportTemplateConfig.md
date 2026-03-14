
# ReportTemplateConfig

`tb_pe_client.models.ReportTemplateConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name_pattern** | **str** |  | [optional] |
| **time_data_pattern** | **str** |  | [optional] |
| **format** | [**TbReportFormat**](TbReportFormat.md) | Report format | |
| **entity_aliases** | [**List[EntityAlias]**](EntityAlias.md) |  | [optional] |
| **filters** | [**List[Filter]**](Filter.md) |  | [optional] |
| **components** | [**List[ReportComponent]**](ReportComponent.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.name_pattern`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportTemplateConfig.model_validate(data)` or `ReportTemplateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

