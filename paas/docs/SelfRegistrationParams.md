
# SelfRegistrationParams

`tb_paas_client.models.SelfRegistrationParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**SelfRegistrationType**](SelfRegistrationType.md) |  | |
| **enabled** | **bool** |  | [optional] |
| **title** | **str** |  | [optional] |
| **captcha** | [**CaptchaParams**](CaptchaParams.md) |  | [optional] |
| **permissions** | [**List[GroupPermission]**](GroupPermission.md) |  | [optional] |
| **notification_recipient** | [**NotificationTargetId**](NotificationTargetId.md) |  | [optional] |
| **sign_up_fields** | [**List[SignUpField]**](SignUpField.md) |  | [optional] |
| **customer_title_prefix** | **str** |  | [optional] |
| **show_privacy_policy** | **bool** |  | [optional] |
| **show_terms_of_use** | **bool** |  | [optional] |
| **default_dashboard** | [**DefaultDashboardParams**](DefaultDashboardParams.md) |  | [optional] |
| **home_dashboard** | [**HomeDashboardParams**](HomeDashboardParams.md) |  | [optional] |
| **customer_group_id** | [**EntityGroupId**](EntityGroupId.md) |  | [optional] |
| **custom_menu_id** | [**CustomMenuId**](CustomMenuId.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`EntityGroupId`, `GroupPermissionId`, `NotificationTargetId`, `RoleId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### SelfRegistrationType (enum)
`WEB` | `MOBILE`

#### CaptchaParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version | str |  |  |

#### GroupPermission
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | GroupPermissionId | JSON object with the Group Permission Id. Specify this field to update the Group Permission. Referencing non-existing Group Permission Id will cause error. Omit this field to create new Group Permission. | [optional] |
| created_time | int | Timestamp of the group permission creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with the Tenant Id. | [optional] [readonly] |
| user_group_id | EntityGroupId | JSON object with the User Group Id. Represents the user group that will have permissions to perform operations against the corresponding entity group. |  |
| role_id | RoleId | JSON object with the Role Id. Represents the set of permissions. The role type (GENERIC or GROUP) determines whether 'entityGroupId' is required. |  |
| entity_group_id | EntityGroupId | JSON object with the Entity Group Id. Required when using a GROUP role — specifies the entity group to which the permissions apply. Must be null or omitted when using a GENERIC role. | [optional] |
| entity_group_type | EntityType | Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc. Auto-populated from the referenced entity group. Null for generic permissions. | [optional] [readonly] |
| is_public | bool |  | [optional] |
| name | str | Name of the Group Permissions. Auto-generated | [optional] [readonly] |
| public | bool |  | [optional] |

#### SignUpField
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | SignUpFieldId | Signup field id |  |
| label | str | Signup field label |  |
| required | bool | Indicates if field is required | [optional] |

#### DefaultDashboardParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str | Default dashboard Id to assign for the new user. | [optional] |
| fullscreen | bool | Set default dashboard to full screen mode. | [optional] |

#### HomeDashboardParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str | Home dashboard Id to assign for the new user. | [optional] |
| hide_toolbar | bool | Indicates if hide toolbar should be hidden. | [optional] |

#### CustomMenuId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### SignUpFieldId (enum)
`EMAIL` | `PASSWORD` | `REPEAT_PASSWORD` | `FIRST_NAME` | `LAST_NAME` | `PHONE` | `COUNTRY` | `CITY` | `STATE` | `ZIP` | … (12 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SelfRegistrationParams.model_validate(data)` or `SelfRegistrationParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

