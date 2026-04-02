
# ShareGroupRequest

`tb_paas_client.models.ShareGroupRequest`

The Share Group Request JSON

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **owner_id** | [**EntityId**](EntityId.md) | In case 'allUserGroup' is set to true, this property specifies the owner of the user group 'All'. Either Tenant or Customer Id. | [optional] |
| **all_user_group** | **bool** | Indicate that the group should be shared with user group 'All' that belongs to Tenant or Customer (see 'ownerId' property description). | |
| **user_group_id** | [**EntityGroupId**](EntityGroupId.md) | In case 'allUserGroup' is set to false, this property specifies the specific user group that the entity group should be shared with. | [optional] |
| **read_else_write** | **bool** | Used if 'roleIds' property is not present. if the value is 'true', creates role with read-only permissions. If the value is 'false', creates role with write permissions. | [optional] |
| **role_ids** | [**List[RoleId]**](RoleId.md) | List of group role Ids that should be used to share the entity group with the user group. If not set, the platform will create new role (see 'readElseWrite' property description) | [optional] |



## Referenced Types

> **EntityId types** (`EntityGroupId`, `RoleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.owner_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ShareGroupRequest.model_validate(data)` or `ShareGroupRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

