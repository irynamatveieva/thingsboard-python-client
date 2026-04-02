
# GroupPermission

`tb_paas_client.models.GroupPermission`

A JSON value representing the group permission.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**GroupPermissionId**](GroupPermissionId.md) | JSON object with the Group Permission Id. Specify this field to update the Group Permission. Referencing non-existing Group Permission Id will cause error. Omit this field to create new Group Permission. | [optional] |
| **created_time** | **int** | Timestamp of the group permission creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with the Tenant Id. | [optional] [readonly] |
| **user_group_id** | [**EntityGroupId**](EntityGroupId.md) | JSON object with the User Group Id. Represents the user group that will have permissions to perform operations against the corresponding entity group. | |
| **role_id** | [**RoleId**](RoleId.md) | JSON object with the Role Id. Represents the set of permissions. The role type (GENERIC or GROUP) determines whether 'entityGroupId' is required. | |
| **entity_group_id** | [**EntityGroupId**](EntityGroupId.md) | JSON object with the Entity Group Id. Required when using a GROUP role — specifies the entity group to which the permissions apply. Must be null or omitted when using a GENERIC role. | [optional] |
| **entity_group_type** | [**EntityType**](EntityType.md) | Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc. Auto-populated from the referenced entity group. Null for generic permissions. | [optional] [readonly] |
| **is_public** | **bool** |  | [optional] |
| **name** | **str** | Name of the Group Permissions. Auto-generated | [optional] [readonly] |
| **public** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `GroupPermission.model_validate(data)` or `GroupPermission.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

