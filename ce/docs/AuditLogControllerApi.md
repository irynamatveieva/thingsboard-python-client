# AuditLogControllerApi

`ThingsboardClient` methods:

```python
PageDataAuditLog client.get_audit_logs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)  # Get all audit logs (getAuditLogs)
PageDataAuditLog client.get_audit_logs_by_customer_id(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)  # Get audit logs by customer id (getAuditLogsByCustomerId)
PageDataAuditLog client.get_audit_logs_by_entity_id(entity_type: str, entity_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)  # Get audit logs by entity id (getAuditLogsByEntityId)
PageDataAuditLog client.get_audit_logs_by_user_id(user_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)  # Get audit logs by user id (getAuditLogsByUserId)
```


## get_audit_logs

```python
PageDataAuditLog client.get_audit_logs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)
```

**GET** `/api/audit/logs`

Get all audit logs (getAuditLogs)

Returns a page of audit logs related to all entities in the scope of the current user's Tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on one of the next properties: entityType, entityName, userName, actionType, actionStatus. | [optional] |
| **sort_property** | **str** | Property of audit log to sort by. See the 'Model' tab of the Response Class for more details. Note: entityType sort property is not defined in the AuditLog class, however, it can be used to sort audit logs by types of entities that were logged. | [optional] [enum: createdTime, entityType, entityName, userName, actionType, actionStatus] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **action_types** | **str** | A String value representing comma-separated list of action types. This parameter is optional, but it can be used to filter results to fetch only audit logs of specific action types. For example, 'LOGIN', 'LOGOUT'. See the 'Model' tab of the Response Class for more details. | [optional] |

### Return type

**PageDataAuditLog**


## get_audit_logs_by_customer_id

```python
PageDataAuditLog client.get_audit_logs_by_customer_id(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)
```

**GET** `/api/audit/logs/customer/{customerId}`

Get audit logs by customer id (getAuditLogsByCustomerId)

Returns a page of audit logs related to the targeted customer entities (devices, assets, etc.), and users actions (login, logout, etc.) that belong to this customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on one of the next properties: entityType, entityName, userName, actionType, actionStatus. | [optional] |
| **sort_property** | **str** | Property of audit log to sort by. See the 'Model' tab of the Response Class for more details. Note: entityType sort property is not defined in the AuditLog class, however, it can be used to sort audit logs by types of entities that were logged. | [optional] [enum: createdTime, entityType, entityName, userName, actionType, actionStatus] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **action_types** | **str** | A String value representing comma-separated list of action types. This parameter is optional, but it can be used to filter results to fetch only audit logs of specific action types. For example, 'LOGIN', 'LOGOUT'. See the 'Model' tab of the Response Class for more details. | [optional] |

### Return type

**PageDataAuditLog**


## get_audit_logs_by_entity_id

```python
PageDataAuditLog client.get_audit_logs_by_entity_id(entity_type: str, entity_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)
```

**GET** `/api/audit/logs/entity/{entityType}/{entityId}`

Get audit logs by entity id (getAuditLogsByEntityId)

Returns a page of audit logs related to the actions on the targeted entity. Basically, this API call is used to get the full lifecycle of some specific entity. For example to see when a device was created, updated, assigned to some customer, or even deleted from the system. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on one of the next properties: entityType, entityName, userName, actionType, actionStatus. | [optional] |
| **sort_property** | **str** | Property of audit log to sort by. See the 'Model' tab of the Response Class for more details. Note: entityType sort property is not defined in the AuditLog class, however, it can be used to sort audit logs by types of entities that were logged. | [optional] [enum: createdTime, entityType, entityName, userName, actionType, actionStatus] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **action_types** | **str** | A String value representing comma-separated list of action types. This parameter is optional, but it can be used to filter results to fetch only audit logs of specific action types. For example, 'LOGIN', 'LOGOUT'. See the 'Model' tab of the Response Class for more details. | [optional] |

### Return type

**PageDataAuditLog**


## get_audit_logs_by_user_id

```python
PageDataAuditLog client.get_audit_logs_by_user_id(user_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None)
```

**GET** `/api/audit/logs/user/{userId}`

Get audit logs by user id (getAuditLogsByUserId)

Returns a page of audit logs related to the actions of targeted user. For example, RPC call to a particular device, or alarm acknowledgment for a specific device, etc. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on one of the next properties: entityType, entityName, userName, actionType, actionStatus. | [optional] |
| **sort_property** | **str** | Property of audit log to sort by. See the 'Model' tab of the Response Class for more details. Note: entityType sort property is not defined in the AuditLog class, however, it can be used to sort audit logs by types of entities that were logged. | [optional] [enum: createdTime, entityType, entityName, userName, actionType, actionStatus] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the AuditLog class field: 'createdTime'. | [optional] |
| **action_types** | **str** | A String value representing comma-separated list of action types. This parameter is optional, but it can be used to filter results to fetch only audit logs of specific action types. For example, 'LOGIN', 'LOGOUT'. See the 'Model' tab of the Response Class for more details. | [optional] |

### Return type

**PageDataAuditLog**

