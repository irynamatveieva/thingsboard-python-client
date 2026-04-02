
# OtherConfiguration

`tb_ce_client.models.OtherConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **power_mode** | [**PowerMode**](PowerMode.md) |  | [optional] |
| **psm_activity_timer** | **int** |  | [optional] |
| **edrx_cycle** | **int** |  | [optional] |
| **paging_transmission_window** | **int** |  | [optional] |
| **use_object19_for_ota_info** | **bool** |  | [optional] |
| **fw_update_strategy** | **int** |  | [optional] |
| **sw_update_strategy** | **int** |  | [optional] |
| **client_only_observe_after_connect** | **int** |  | [optional] |
| **fw_update_resource** | **str** |  | [optional] |
| **sw_update_resource** | **str** |  | [optional] |
| **default_object_id_ver** | **str** |  | [optional] |



## Referenced Types

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.power_mode`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OtherConfiguration.model_validate(data)` or `OtherConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

