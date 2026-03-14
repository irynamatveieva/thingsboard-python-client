
# DataKeyComparisonSettings

`tb_pe_client.models.DataKeyComparisonSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_values_for_comparison** | **bool** |  | [optional] |
| **comparison_values_label** | **str** |  | [optional] |
| **color** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.show_values_for_comparison`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DataKeyComparisonSettings.model_validate(data)` or `DataKeyComparisonSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

