
# EntityGroupExportData

`tb_pe_client.models.EntityGroupExportData`

**Extends:** **EntityExportData**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **permissions** | [**List[GroupPermission]**](GroupPermission.md) |  | [optional] |
| **group_ota_packages** | [**List[DeviceGroupOtaPackage]**](DeviceGroupOtaPackage.md) |  | [optional] |
| **group_entities** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.permissions`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityGroupExportData.model_validate(data)` or `EntityGroupExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

