
# PowerSavingConfiguration

`tb_pe_client.models.PowerSavingConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **power_mode** | [**PowerMode**](PowerMode.md) |  | [optional] |
| **psm_activity_timer** | **int** |  | [optional] |
| **edrx_cycle** | **int** |  | [optional] |
| **paging_transmission_window** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.power_mode`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PowerSavingConfiguration.model_validate(data)` or `PowerSavingConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

