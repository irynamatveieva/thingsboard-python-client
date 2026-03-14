
# AllowedPermissionsInfo

`tb_paas_client.models.AllowedPermissionsInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operations_by_resource** | **Dict[str, List[Operation]]** | Static map (vocabulary) of allowed operations by resource type | [optional] |
| **allowed_for_group_role_operations** | [**List[Operation]**](Operation.md) | Static set (vocabulary) of allowed operations for group roles | [optional] |
| **allowed_for_group_owner_only_operations** | [**List[Operation]**](Operation.md) | Static set (vocabulary) of allowed operations for group owner | [optional] |
| **allowed_for_group_owner_only_group_operations** | [**List[Operation]**](Operation.md) | Static set (vocabulary) of allowed group operations for group owner | [optional] |
| **allowed_resources** | [**List[Resource]**](Resource.md) | Static set (vocabulary) of all possibly allowed resources. Static and depends only on the authority of the user | [optional] |
| **user_permissions** | [**MergedUserPermissions**](MergedUserPermissions.md) | JSON object with merged permission for all generic and group roles assigned to all user groups the user belongs to | [optional] |
| **user_owner_id** | [**EntityId**](EntityId.md) | Owner Id of the user (Tenant or Customer) | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.operations_by_resource`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AllowedPermissionsInfo.model_validate(data)` or `AllowedPermissionsInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

