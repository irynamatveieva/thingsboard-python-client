# NotificationTargetControllerApi

`ThingsboardClient` methods:

```python
None client.delete_notification_target_by_id(id: UUID)  # Delete notification target by id (deleteNotificationTargetById)
NotificationTarget client.get_notification_target_by_id(id: UUID)  # Get notification target by id (getNotificationTargetById)
PageDataNotificationTarget client.get_notification_targets(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get notification targets (getNotificationTargets)
List[NotificationTarget] client.get_notification_targets_by_ids(ids: List[str])  # Get notification targets by ids (getNotificationTargetsByIds)
PageDataNotificationTarget client.get_notification_targets_by_supported_notification_type(notification_type: NotificationType, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get notification targets by supported notification type (getNotificationTargetsBySupportedNotificationType)
PageDataUser client.get_recipients_for_notification_target_config(page_size: int, page: int, notification_target: NotificationTarget)  # Get recipients for notification target config (getRecipientsForNotificationTargetConfig)
NotificationTarget client.save_notification_target(notification_target: NotificationTarget)  # Save notification target (saveNotificationTarget)
```


## delete_notification_target_by_id

```python
None client.delete_notification_target_by_id(id: UUID)
```

**DELETE** `/api/notification/target/{id}`

Delete notification target by id (deleteNotificationTargetById)

Deletes notification target by its id.  This target cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_notification_target_by_id

```python
NotificationTarget client.get_notification_target_by_id(id: UUID)
```

**GET** `/api/notification/target/{id}`

Get notification target by id (getNotificationTargetById)

Fetches notification target by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**NotificationTarget**


## get_notification_targets

```python
PageDataNotificationTarget client.get_notification_targets(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/notification/targets`

Get notification targets (getNotificationTargets)

Returns the page of notification targets owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filed based on the target's name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataNotificationTarget**


## get_notification_targets_by_ids

```python
List[NotificationTarget] client.get_notification_targets_by_ids(ids: List[str])
```

**GET** `/api/notification/targets/list`

Get notification targets by ids (getNotificationTargetsByIds)

Returns the list of notification targets found by provided ids.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ids** | **List[str]** | Comma-separated list of uuids representing targets ids | |

### Return type

**List[NotificationTarget]**


## get_notification_targets_by_supported_notification_type

```python
PageDataNotificationTarget client.get_notification_targets_by_supported_notification_type(notification_type: NotificationType, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/notification/targets/notificationType/{notificationType}`

Get notification targets by supported notification type (getNotificationTargetsBySupportedNotificationType)

Returns the page of notification targets filtered by notification type that they can be used for.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **notification_type** | **NotificationType** |  | [enum: GENERAL, ALARM, DEVICE_ACTIVITY, ENTITY_ACTION, ALARM_COMMENT, RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT, ALARM_ASSIGNMENT, NEW_PLATFORM_VERSION, ENTITIES_LIMIT, ENTITIES_LIMIT_INCREASE_REQUEST, API_USAGE_LIMIT, RULE_NODE, RATE_LIMITS, EDGE_CONNECTION, EDGE_COMMUNICATION_FAILURE, TASK_PROCESSING_FAILURE, RESOURCES_SHORTAGE] |
| **page_size** | **int** |  | |
| **page** | **int** |  | |
| **text_search** | **str** |  | [optional] |
| **sort_property** | **str** |  | [optional] |
| **sort_order** | **str** |  | [optional] |

### Return type

**PageDataNotificationTarget**


## get_recipients_for_notification_target_config

```python
PageDataUser client.get_recipients_for_notification_target_config(page_size: int, page: int, notification_target: NotificationTarget)
```

**POST** `/api/notification/target/recipients`

Get recipients for notification target config (getRecipientsForNotificationTargetConfig)

Returns the page of recipients for such notification target configuration.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **notification_target** | **NotificationTarget** |  | |

### Return type

**PageDataUser**


## save_notification_target

```python
NotificationTarget client.save_notification_target(notification_target: NotificationTarget)
```

**POST** `/api/notification/target`

Save notification target (saveNotificationTarget)

Creates or updates notification target.  Available `configuration` types are `PLATFORM_USERS` and `SLACK`. For `PLATFORM_USERS` the `usersFilter` must be specified. For tenant, there are following users filter types available: `USER_LIST`, `CUSTOMER_USERS`, `TENANT_ADMINISTRATORS`, `ALL_USERS`, `ORIGINATOR_ENTITY_OWNER_USERS`, `AFFECTED_USER`. For sysadmin: `TENANT_ADMINISTRATORS`, `AFFECTED_TENANT_ADMINISTRATORS`, `SYSTEM_ADMINISTRATORS`, `ALL_USERS`.  Here is an example of tenant-level notification target to send notification to customer's users: ```json {   \"name\": \"Users of Customer A\",   \"configuration\": {     \"type\": \"PLATFORM_USERS\",     \"usersFilter\": {       \"type\": \"CUSTOMER_USERS\",       \"customerId\": \"32499a20-d785-11ed-a06c-21dd57dd88ca\"     },     \"description\": \"Users of Customer A\"   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **notification_target** | **NotificationTarget** |  | |

### Return type

**NotificationTarget**

