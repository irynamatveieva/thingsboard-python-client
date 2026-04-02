
# MobileAppBundle

`tb_paas_client.models.MobileAppBundle`

A JSON value representing the Mobile Application Bundle.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**MobileAppBundleId**](MobileAppBundleId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] |
| **title** | **str** | Application bundle title. Cannot be empty | |
| **description** | **str** | Application bundle description. | [optional] |
| **android_app_id** | [**MobileAppId**](MobileAppId.md) | Android application id | [optional] |
| **ios_app_id** | [**MobileAppId**](MobileAppId.md) | IOS application id | [optional] |
| **layout_config** | [**MobileLayoutConfig**](MobileLayoutConfig.md) | Application layout configuration | [optional] |
| **self_registration_params** | [**MobileSelfRegistrationParams**](MobileSelfRegistrationParams.md) | Application self registration configuration | [optional] |
| **oauth2_enabled** | **bool** | Whether OAuth2 settings are enabled or not | [optional] |
| **name** | **str** | Mobile app bundle title | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`EntityGroupId`, `GroupPermissionId`, `MobileAppBundleId`, `MobileAppId`, `NotificationTargetId`, `RoleId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### MobileLayoutConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| pages | List[MobilePage] |  | [optional] |

#### MobileSelfRegistrationParams  *(extends SelfRegistrationParams)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| privacy_policy | str | Privacy policy text. Supports HTML. | [optional] |
| redirect | MobileRedirectParams | Mobile redirect params. |  |
| terms_of_use | str | Terms of User text. Supports HTML. | [optional] |

#### MobilePage
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | MobilePageType |  |  |
| visible | bool |  | [optional] |

#### SelfRegistrationParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | SelfRegistrationType |  |  |
| enabled | bool |  | [optional] |
| title | str |  | [optional] |
| captcha | CaptchaParams |  | [optional] |
| permissions | List[GroupPermission] |  | [optional] |
| notification_recipient | NotificationTargetId |  | [optional] |
| sign_up_fields | List[SignUpField] |  | [optional] |
| customer_title_prefix | str |  | [optional] |
| show_privacy_policy | bool |  | [optional] |
| show_terms_of_use | bool |  | [optional] |
| default_dashboard | DefaultDashboardParams |  | [optional] |
| home_dashboard | HomeDashboardParams |  | [optional] |
| customer_group_id | EntityGroupId |  | [optional] |
| custom_menu_id | CustomMenuId |  | [optional] |

#### MobileRedirectParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| scheme | str | Mobile application verification settings. Used for callback to mobile application once user is registered. | [optional] |
| host | str | Mobile application verification settings. Used for callback to mobile application once user is registered. | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### MobilePageType (enum)
`DEFAULT` | `DASHBOARD` | `WEB_VIEW` | `CUSTOM`

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

#### SignUpFieldId (enum)
`EMAIL` | `PASSWORD` | `REPEAT_PASSWORD` | `FIRST_NAME` | `LAST_NAME` | `PHONE` | `COUNTRY` | `CITY` | `STATE` | `ZIP` | … (12 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileAppBundle.model_validate(data)` or `MobileAppBundle.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

