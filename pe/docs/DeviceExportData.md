
# DeviceExportData

`tb_pe_client.models.DeviceExportData`

**Extends:** **EntityExportData**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **credentials** | [**DeviceCredentials**](DeviceCredentials.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.credentials`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceExportData.model_validate(data)` or `DeviceExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

