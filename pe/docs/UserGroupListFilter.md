
# UserGroupListFilter

`tb_pe_client.models.UserGroupListFilter`

**Extends:** **UsersFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **groups_ids** | **List[UUID]** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.groups_ids`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserGroupListFilter.model_validate(data)` or `UserGroupListFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

