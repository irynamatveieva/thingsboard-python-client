# RoleControllerApi

`ThingsboardClient` methods:

```python
None client.delete_role(role_id: str)  # Delete role (deleteRole)
Role client.get_role_by_id(role_id: str)  # Get Role by Id (getRoleById)
PageDataRole client.get_roles(page_size: str, page: str, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Roles (getRoles)
List[Role] client.get_roles_by_ids(role_ids: List[str])  # Get Roles By Ids (getRolesByIds)
Role client.save_role(role: Role)  # Create Or Update Role (saveRole)
```


## delete_role

```python
None client.delete_role(role_id: str)
```

**DELETE** `/api/role/{roleId}`

Delete role (deleteRole)

Deletes the role. Referencing non-existing role Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str** | A string value representing the role id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_role_by_id

```python
Role client.get_role_by_id(role_id: str)
```

**GET** `/api/role/{roleId}`

Get Role by Id (getRoleById)

Fetch the Role object based on the provided Role Id. Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller). Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str** | A string value representing the role id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Role**


## get_roles

```python
PageDataRole client.get_roles(page_size: str, page: str, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/roles`

Get Roles (getRoles)

Returns a page of roles that are available for the current user. Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller).You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **type** | **str** | Type of the role | [optional] [enum: GENERIC, GROUP] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the role name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, description] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataRole**


## get_roles_by_ids

```python
List[Role] client.get_roles_by_ids(role_ids: List[str])
```

**GET** `/api/roles/list`

Get Roles By Ids (getRolesByIds)

Returns the list of rows based on their ids.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **role_ids** | **List[str]** | A list of role ids, separated by comma ',' | |

### Return type

**List[Role]**


## save_role

```python
Role client.save_role(role: Role)
```

**POST** `/api/role`

Create Or Update Role (saveRole)

Creates or Updates the Role. When creating Role, platform generates Role Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Role id will be present in the response. Specify existing Role id to update the permission. Referencing non-existing Group Permission Id will cause 'Not Found' error.  Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller).  Example of Generic Role with read-only permissions for any resource and all permissions for the 'DEVICE' and 'PROFILE' resources is listed below:   ```json {   \"name\": \"Read-Only User\",   \"type\": \"GENERIC\",   \"permissions\": {     \"ALL\": [       \"READ\",       \"RPC_CALL\",       \"READ_CREDENTIALS\",       \"READ_ATTRIBUTES\",       \"READ_TELEMETRY\"     ],     \"DEVICE\": [       \"ALL\"     ]     \"PROFILE\": [       \"ALL\"     ]   },   \"additionalInfo\": {     \"description\": \"Read-only permissions for everything, Write permissions for devices and own profile.\"   } } ```  Example of Group Role with read-only permissions. Note that the group role has no association with the resources. The type of the resource is taken from the entity group that this role is assigned to:   ```json {   \"name\": \"Entity Group Read-only User\",   \"type\": \"GROUP\",   \"permissions\": [     \"READ\",     \"RPC_CALL\",     \"READ_CREDENTIALS\",     \"READ_ATTRIBUTES\",     \"READ_TELEMETRY\"   ],   \"additionalInfo\": {     \"description\": \"Read-only permissions.\"   } } ```   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **role** | **Role** |  | |

### Return type

**Role**

