
# PdfReportTemplateConfig

`tb_pe_client.models.PdfReportTemplateConfig`

**Extends:** **ReportTemplateConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **footer** | [**HeaderFooter**](HeaderFooter.md) |  | [optional] |
| **header** | [**HeaderFooter**](HeaderFooter.md) |  | [optional] |
| **page_background** | **str** |  | [optional] |
| **page_margins** | [**Insets**](Insets.md) |  | [optional] |
| **page_orientation** | [**PageOrientation**](PageOrientation.md) |  | [optional] |
| **page_size** | [**PageSize**](PageSize.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.footer`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PdfReportTemplateConfig.model_validate(data)` or `PdfReportTemplateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

