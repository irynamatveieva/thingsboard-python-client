
# CfReprocessingJobConfiguration

`tb_pe_client.models.CfReprocessingJobConfiguration`

**Extends:** **JobConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **calculated_field_id** | [**CalculatedFieldId**](CalculatedFieldId.md) |  | |
| **calculated_field_name** | **str** |  | [optional] |
| **start_ts** | **int** |  | [optional] |
| **end_ts** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.calculated_field_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CfReprocessingJobConfiguration.model_validate(data)` or `CfReprocessingJobConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

