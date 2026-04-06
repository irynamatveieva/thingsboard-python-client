
# PlatformUsersNotificationTargetConfig

`tb_paas_client.models.PlatformUsersNotificationTargetConfig`

**Extends:** **NotificationTargetConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **users_filter** | [**UsersFilter**](UsersFilter.md) |  | |



## Referenced Types

#### NotificationTargetConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| description | str |  | [optional] |
| type | str |  |  |

#### UsersFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AffectedTenantAdministratorsFilter  *(extends UsersFilter, type=`AFFECTED_TENANT_ADMINISTRATORS`)*
*See UsersFilter for properties.*

#### AffectedUserFilter  *(extends UsersFilter, type=`AFFECTED_USER`)*
*See UsersFilter for properties.*

#### AllUsersFilter  *(extends UsersFilter, type=`ALL_USERS`)*
*See UsersFilter for properties.*

#### CustomerUsersFilter  *(extends UsersFilter, type=`CUSTOMER_USERS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| customer_id | UUID |  |  |

#### OriginatorEntityOwnerUsersFilter  *(extends UsersFilter, type=`ORIGINATOR_ENTITY_OWNER_USERS`)*
*See UsersFilter for properties.*

#### SystemAdministratorsFilter  *(extends UsersFilter, type=`SYSTEM_ADMINISTRATORS`)*
*See UsersFilter for properties.*

#### TenantAdministratorsFilter  *(extends UsersFilter, type=`TENANT_ADMINISTRATORS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tenants_ids | List[UUID] |  | [optional] |
| tenant_profiles_ids | List[UUID] |  | [optional] |

#### UserGroupListFilter  *(extends UsersFilter, type=`USER_GROUP_LIST`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| groups_ids | List[UUID] |  |  |

#### UserListFilter  *(extends UsersFilter, type=`USER_LIST`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| users_ids | List[UUID] |  |  |

#### UserRoleFilter  *(extends UsersFilter, type=`USER_ROLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| roles_ids | List[UUID] |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.users_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PlatformUsersNotificationTargetConfig.model_validate(data)` or `PlatformUsersNotificationTargetConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

