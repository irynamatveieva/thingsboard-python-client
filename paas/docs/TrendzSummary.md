
# TrendzSummary

`tb_paas_client.models.TrendzSummary`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **metric_summary_items** | **List[object]** |  | [optional] |
| **anomaly_model_summary_items** | **List[object]** |  | [optional] |
| **calculation_field_summary_items** | **List[object]** |  | [optional] |
| **prediction_model_summary_items** | **List[object]** |  | [optional] |
| **view_summary_items** | **List[object]** |  | [optional] |
| **ai_summary_items** | **List[object]** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.metric_summary_items`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzSummary.model_validate(data)` or `TrendzSummary.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

