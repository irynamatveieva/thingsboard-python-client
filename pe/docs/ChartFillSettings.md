
# ChartFillSettings

`tb_pe_client.models.ChartFillSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**ChartFillType**](ChartFillType.md) |  | [optional] |
| **opacity** | **float** |  | [optional] |
| **gradient** | [**ChartFillSettingsGradient**](ChartFillSettingsGradient.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ChartFillSettings.model_validate(data)` or `ChartFillSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

