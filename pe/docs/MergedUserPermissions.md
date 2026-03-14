
# MergedUserPermissions

`tb_pe_client.models.MergedUserPermissions`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **generic_permissions** | **Dict[str, List[Operation]]** | Map of permissions defined using generic roles ('Customer Administrator', etc) | [optional] |
| **group_permissions** | [**Dict[str, MergedGroupPermissionInfo]**](MergedGroupPermissionInfo.md) | Map of permissions defined using group roles ('Read' or 'Write' access to specific entity group, etc) | [optional] |
| **read_group_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read permissions per entity type. Used on the UI to enable/disable certain components. | [optional] |
| **read_entity_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read permissions per resource. Used on the UI to enable/disable certain components. | [optional] |
| **read_attr_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read entity attributes permissions per resource. Used on the UI to enable/disable certain tabs. | [optional] |
| **read_ts_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read entity time-series permissions per resource. Used on the UI to enable/disable certain tabs. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.generic_permissions`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MergedUserPermissions.model_validate(data)` or `MergedUserPermissions.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

