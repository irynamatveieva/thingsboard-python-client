
# TimeSeriesChartGridSettings

`tb_paas_client.models.TimeSeriesChartGridSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show** | **bool** |  | [optional] |
| **background_color** | **str** |  | [optional] |
| **border_width** | **float** |  | [optional] |
| **border_color** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.show`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesChartGridSettings.model_validate(data)` or `TimeSeriesChartGridSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

