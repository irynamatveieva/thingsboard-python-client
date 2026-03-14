
# HeaderFooter

`tb_paas_client.models.HeaderFooter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** |  | [optional] |
| **components** | [**List[ReportComponent]**](ReportComponent.md) |  | |
| **first_page** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `HeaderFooter.model_validate(data)` or `HeaderFooter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

