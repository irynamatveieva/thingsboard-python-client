
# QRCodeConfig

`tb_paas_client.models.QRCodeConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_on_home_page** | **bool** |  | [optional] |
| **badge_enabled** | **bool** |  | [optional] |
| **qr_code_label_enabled** | **bool** |  | [optional] |
| **badge_position** | [**BadgePosition**](BadgePosition.md) |  | [optional] |
| **qr_code_label** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.show_on_home_page`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `QRCodeConfig.model_validate(data)` or `QRCodeConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

