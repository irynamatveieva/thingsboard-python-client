
# UsersFilter

`tb_ce_client.models.UsersFilter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### AffectedTenantAdministratorsFilter  *(type=`AFFECTED_TENANT_ADMINISTRATORS`)*
*(no additional properties)*

#### AffectedUserFilter  *(type=`AFFECTED_USER`)*
*(no additional properties)*

#### AllUsersFilter  *(type=`ALL_USERS`)*
*(no additional properties)*

#### CustomerUsersFilter  *(type=`CUSTOMER_USERS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| customer_id | UUID |  |  |

#### OriginatorEntityOwnerUsersFilter  *(type=`ORIGINATOR_ENTITY_OWNER_USERS`)*
*(no additional properties)*

#### SystemAdministratorsFilter  *(type=`SYSTEM_ADMINISTRATORS`)*
*(no additional properties)*

#### TenantAdministratorsFilter  *(type=`TENANT_ADMINISTRATORS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tenants_ids | List[UUID] |  | [optional] |
| tenant_profiles_ids | List[UUID] |  | [optional] |

#### UserListFilter  *(type=`USER_LIST`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| users_ids | List[UUID] |  |  |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UsersFilter.model_validate(data)` or `UsersFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

