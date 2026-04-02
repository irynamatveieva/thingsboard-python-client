
# LegendConfig

`tb_paas_client.models.LegendConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **position** | [**LegendPosition**](LegendPosition.md) |  | [optional] |
| **sort_data_keys** | **bool** |  | [optional] |
| **show_min** | **bool** |  | [optional] |
| **show_max** | **bool** |  | [optional] |
| **show_avg** | **bool** |  | [optional] |
| **show_total** | **bool** |  | [optional] |
| **show_latest** | **bool** |  | [optional] |



## Referenced Types

#### LegendPosition (enum)
`TOP` | `BOTTOM` | `LEFT` | `RIGHT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.position`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LegendConfig.model_validate(data)` or `LegendConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

