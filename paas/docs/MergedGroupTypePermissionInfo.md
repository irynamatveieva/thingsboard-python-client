
# MergedGroupTypePermissionInfo

`tb_paas_client.models.MergedGroupTypePermissionInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_group_ids** | [**List[EntityGroupId]**](EntityGroupId.md) | List of Entity Groups in case of group roles are assigned to the user (user group) | [optional] |
| **has_generic_read** | **bool** | Indicates if generic permission assigned to the user group. | [optional] |



## Referenced Types

> **EntityId types** (`EntityGroupId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_group_ids`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MergedGroupTypePermissionInfo.model_validate(data)` or `MergedGroupTypePermissionInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

