
# ReportDoughnutChartSettings

`tb_paas_client.models.ReportDoughnutChartSettings`

**Extends:** **ReportLatestChartSettings**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **layout** | [**DoughnutLayout**](DoughnutLayout.md) |  | [optional] |
| **clockwise** | **bool** |  | [optional] |
| **total_value_font** | [**Font**](Font.md) |  | [optional] |
| **total_value_color** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.layout`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportDoughnutChartSettings.model_validate(data)` or `ReportDoughnutChartSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

