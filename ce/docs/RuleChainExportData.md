
# RuleChainExportData

`tb_ce_client.models.RuleChainExportData`

**Extends:** **EntityExportData**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **meta_data** | [**RuleChainMetaData**](RuleChainMetaData.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.meta_data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainExportData.model_validate(data)` or `RuleChainExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

