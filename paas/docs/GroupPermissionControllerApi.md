# GroupPermissionControllerApi

`ThingsboardClient` methods:

```python
None client.delete_group_permission(group_permission_id: str)  # Delete group permission (deleteGroupPermission)
List[GroupPermissionInfo] client.get_entity_group_permissions(entity_group_id: str)  # Get group permissions by Entity Group Id (getEntityGroupPermissions)
GroupPermission client.get_group_permission_by_id(group_permission_id: str)  # Get Group Permission (getGroupPermissionById)
GroupPermissionInfo client.get_group_permission_info_by_id(group_permission_id: str, is_user_group: bool)  # Get Group Permission Info (getGroupPermissionInfoById)
List[GroupPermissionInfo] client.get_user_group_permissions(user_group_id: str)  # Get group permissions by User Group Id (getUserGroupPermissions)
List[GroupPermissionInfo] client.load_user_group_permission_infos(group_permission: List[GroupPermission])  # Load User Group Permissions (loadUserGroupPermissionInfos)
GroupPermission client.save_group_permission(group_permission: GroupPermission)  # Create Or Update Group Permission (saveGroupPermission)
```


## delete_group_permission

```python
None client.delete_group_permission(group_permission_id: str)
```

**DELETE** `/api/groupPermission/{groupPermissionId}`

Delete group permission (deleteGroupPermission)

Deletes the group permission. Referencing non-existing group permission Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_permission_id** | **str** | A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_entity_group_permissions

```python
List[GroupPermissionInfo] client.get_entity_group_permissions(entity_group_id: str)
```

**GET** `/api/entityGroup/{entityGroupId}/groupPermissions`

Get group permissions by Entity Group Id (getEntityGroupPermissions)

Returns a list of group permission objects that is assigned for the specified Entity Group Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;  There are two types of group permissions depending on the Role type:    * **Generic permission** — uses a GENERIC role. The 'entityGroupId' field must be null (or omitted). Grants the role's operations to all entities within the owner's scope (all tenant entities for tenant admins, only customer-owned entities for customer users).  * **Group permission** — uses a GROUP role. The 'entityGroupId' field must reference a valid entity group. Grants the role's operations only to entities in the specified group.  Assigning a GENERIC role with a non-null 'entityGroupId' will cause an error. The 'entityGroupType' field is auto-populated from the referenced entity group and should not be set manually. Duplicate permissions (same userGroupId + roleId + entityGroupId combination) are rejected.   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[GroupPermissionInfo]**


## get_group_permission_by_id

```python
GroupPermission client.get_group_permission_by_id(group_permission_id: str)
```

**GET** `/api/groupPermission/{groupPermissionId}`

Get Group Permission (getGroupPermissionById)

Fetch the Group Permission object based on the provided Group Permission Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;  There are two types of group permissions depending on the Role type:    * **Generic permission** — uses a GENERIC role. The 'entityGroupId' field must be null (or omitted). Grants the role's operations to all entities within the owner's scope (all tenant entities for tenant admins, only customer-owned entities for customer users).  * **Group permission** — uses a GROUP role. The 'entityGroupId' field must reference a valid entity group. Grants the role's operations only to entities in the specified group.  Assigning a GENERIC role with a non-null 'entityGroupId' will cause an error. The 'entityGroupType' field is auto-populated from the referenced entity group and should not be set manually. Duplicate permissions (same userGroupId + roleId + entityGroupId combination) are rejected.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_permission_id** | **str** | A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**GroupPermission**


## get_group_permission_info_by_id

```python
GroupPermissionInfo client.get_group_permission_info_by_id(group_permission_id: str, is_user_group: bool)
```

**GET** `/api/groupPermission/info/{groupPermissionId}`

Get Group Permission Info (getGroupPermissionInfoById)

Fetch the Group Permission Info object based on the provided Group Permission Id and the flag that controls what additional information to load: User or Entity Group. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;  There are two types of group permissions depending on the Role type:    * **Generic permission** — uses a GENERIC role. The 'entityGroupId' field must be null (or omitted). Grants the role's operations to all entities within the owner's scope (all tenant entities for tenant admins, only customer-owned entities for customer users).  * **Group permission** — uses a GROUP role. The 'entityGroupId' field must reference a valid entity group. Grants the role's operations only to entities in the specified group.  Assigning a GENERIC role with a non-null 'entityGroupId' will cause an error. The 'entityGroupType' field is auto-populated from the referenced entity group and should not be set manually. Duplicate permissions (same userGroupId + roleId + entityGroupId combination) are rejected.   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.  Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_permission_id** | **str** | A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **is_user_group** | **bool** | Load additional information about User('true') or Entity Group('false). | |

### Return type

**GroupPermissionInfo**


## get_user_group_permissions

```python
List[GroupPermissionInfo] client.get_user_group_permissions(user_group_id: str)
```

**GET** `/api/userGroup/{userGroupId}/groupPermissions`

Get group permissions by User Group Id (getUserGroupPermissions)

Returns a list of group permission objects that belongs to specified User Group Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;  There are two types of group permissions depending on the Role type:    * **Generic permission** — uses a GENERIC role. The 'entityGroupId' field must be null (or omitted). Grants the role's operations to all entities within the owner's scope (all tenant entities for tenant admins, only customer-owned entities for customer users).  * **Group permission** — uses a GROUP role. The 'entityGroupId' field must reference a valid entity group. Grants the role's operations only to entities in the specified group.  Assigning a GENERIC role with a non-null 'entityGroupId' will cause an error. The 'entityGroupType' field is auto-populated from the referenced entity group and should not be set manually. Duplicate permissions (same userGroupId + roleId + entityGroupId combination) are rejected.   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[GroupPermissionInfo]**


## load_user_group_permission_infos

```python
List[GroupPermissionInfo] client.load_user_group_permission_infos(group_permission: List[GroupPermission])
```

**POST** `/api/userGroup/groupPermissions/info`

Load User Group Permissions (loadUserGroupPermissionInfos)

Enrich a list of group permission objects with the information about Role, User and Entity Groups. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;  There are two types of group permissions depending on the Role type:    * **Generic permission** — uses a GENERIC role. The 'entityGroupId' field must be null (or omitted). Grants the role's operations to all entities within the owner's scope (all tenant entities for tenant admins, only customer-owned entities for customer users).  * **Group permission** — uses a GROUP role. The 'entityGroupId' field must reference a valid entity group. Grants the role's operations only to entities in the specified group.  Assigning a GENERIC role with a non-null 'entityGroupId' will cause an error. The 'entityGroupType' field is auto-populated from the referenced entity group and should not be set manually. Duplicate permissions (same userGroupId + roleId + entityGroupId combination) are rejected.   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_permission** | **List[GroupPermission]** |  | |

### Return type

**List[GroupPermissionInfo]**


## save_group_permission

```python
GroupPermission client.save_group_permission(group_permission: GroupPermission)
```

**POST** `/api/groupPermission`

Create Or Update Group Permission (saveGroupPermission)

Creates or Updates the Group Permission. When creating group permission, platform generates Group Permission Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Group Permission id will be present in the response. Specify existing Group Permission id to update the permission. Referencing non-existing Group Permission Id will cause 'Not Found' error.  Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;  There are two types of group permissions depending on the Role type:    * **Generic permission** — uses a GENERIC role. The 'entityGroupId' field must be null (or omitted). Grants the role's operations to all entities within the owner's scope (all tenant entities for tenant admins, only customer-owned entities for customer users).  * **Group permission** — uses a GROUP role. The 'entityGroupId' field must reference a valid entity group. Grants the role's operations only to entities in the specified group.  Assigning a GENERIC role with a non-null 'entityGroupId' will cause an error. The 'entityGroupType' field is auto-populated from the referenced entity group and should not be set manually. Duplicate permissions (same userGroupId + roleId + entityGroupId combination) are rejected.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_permission** | **GroupPermission** |  | |

### Return type

**GroupPermission**

