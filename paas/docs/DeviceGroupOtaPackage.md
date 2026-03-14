
# DeviceGroupOtaPackage

`tb_paas_client.models.DeviceGroupOtaPackage`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **UUID** |  | [optional] |
| **group_id** | [**EntityGroupId**](EntityGroupId.md) |  | [optional] |
| **ota_package_type** | [**OtaPackageType**](OtaPackageType.md) |  | [optional] |
| **ota_package_id** | [**OtaPackageId**](OtaPackageId.md) |  | [optional] |
| **ota_package_update_time** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceGroupOtaPackage.model_validate(data)` or `DeviceGroupOtaPackage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

