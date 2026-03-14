
# WidgetsBundleExportData

`tb_ce_client.models.WidgetsBundleExportData`

**Extends:** **EntityExportData**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **widgets** | **List[object]** |  | [optional] |
| **fqns** | **List[str]** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.widgets`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WidgetsBundleExportData.model_validate(data)` or `WidgetsBundleExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

