
# TenantAdministratorsFilter

`tb_paas_client.models.TenantAdministratorsFilter`

**Extends:** **UsersFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tenants_ids** | **List[UUID]** |  | [optional] |
| **tenant_profiles_ids** | **List[UUID]** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.tenants_ids`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantAdministratorsFilter.model_validate(data)` or `TenantAdministratorsFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

