
# LicenseUsageInfo

`tb_paas_client.models.LicenseUsageInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **max_devices** | **int** |  | [optional] |
| **max_assets** | **int** |  | [optional] |
| **white_labeling_enabled** | **bool** |  | [optional] |
| **development** | **bool** |  | [optional] |
| **plan** | **str** |  | [optional] |
| **devices_count** | **int** |  | [optional] |
| **assets_count** | **int** |  | [optional] |
| **dashboards_count** | **int** |  | [optional] |
| **integrations_count** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.max_devices`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LicenseUsageInfo.model_validate(data)` or `LicenseUsageInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

