# NotificationControllerApi

`ThingsboardClient` methods:

```python
NotificationRequest client.create_notification_request(notification_request: NotificationRequest)  # Create notification request (createNotificationRequest)
None client.delete_notification(id: UUID)  # Delete notification (deleteNotification)
None client.delete_notification_request(id: UUID)  # Delete notification request (deleteNotificationRequest)
List[NotificationDeliveryMethod] client.get_available_delivery_methods()  # Get available delivery methods (getAvailableDeliveryMethods)
NotificationRequestInfo client.get_notification_request_by_id(id: UUID)  # Get notification request by id (getNotificationRequestById)
NotificationRequestPreview client.get_notification_request_preview(notification_request: NotificationRequest, recipients_preview_size: Optional[int] = None)  # Get notification request preview (getNotificationRequestPreview)
PageDataNotificationRequestInfo client.get_notification_requests(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get notification requests (getNotificationRequests)
NotificationSettings client.get_notification_settings()  # Get notification settings (getNotificationSettings)
PageDataNotification client.get_notifications(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, unread_only: Optional[bool] = None, delivery_method: Optional[str] = None)  # Get notifications (getNotifications)
int client.get_unread_notifications_count(delivery_method: Optional[str] = None)  # Get unread notifications count (getUnreadNotificationsCount)
UserNotificationSettings client.get_user_notification_settings()  # getUserNotificationSettings
None client.mark_all_notifications_as_read(delivery_method: Optional[str] = None)  # Mark all notifications as read (markAllNotificationsAsRead)
None client.mark_notification_as_read(id: UUID)  # Mark notification as read (markNotificationAsRead)
NotificationSettings client.save_notification_settings(notification_settings: NotificationSettings)  # Save notification settings (saveNotificationSettings)
UserNotificationSettings client.save_user_notification_settings(user_notification_settings: UserNotificationSettings)  # saveUserNotificationSettings
None client.send_addon_access_error(addon_type: str)  # Send add-on access error notification to System/Tenant administrators (sendAddonAccessError)
None client.send_entities_limit_increase_request(entity_type: str)  # Send entity limit increase request notification to System/Tenant administrators (sendEntitiesLimitIncreaseRequest)
```


## create_notification_request

```python
NotificationRequest client.create_notification_request(notification_request: NotificationRequest)
```

**POST** `/api/notification/request`

Create notification request (createNotificationRequest)

Processes notification request. Mandatory request properties are `targets` (list of targets ids to send notification to), and either `templateId` (existing notification template id) or `template` (to send notification without saving the template). Optionally, you can set `sendingDelayInSec` inside the `additionalConfig` field to schedule the notification.  For each enabled delivery method in the notification template, there must be a target in the `targets` list that supports this delivery method: if you chose `WEB`, `EMAIL` or `SMS` - there must be at least one target in `targets` of `PLATFORM_USERS` type. For `SLACK` delivery method - you need to chose at least one `SLACK` notification target.  Notification request object with `PROCESSING` status will be returned immediately, and the notification sending itself is done asynchronously. After all notifications are sent, the `status` of the request becomes `SENT`. Use `getNotificationRequestById` to see the notification request processing status and some sending stats.   Here is an example of notification request to one target using saved template: ```json {   \"templateId\": {     \"entityType\": \"NOTIFICATION_TEMPLATE\",     \"id\": \"6dbc3670-e4dd-11ed-9401-dbcc5dff78be\"   },   \"targets\": [     \"320e3ed0-d785-11ed-a06c-21dd57dd88ca\"   ],   \"additionalConfig\": {     \"sendingDelayInSec\": 0   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **notification_request** | **NotificationRequest** |  | |

### Return type

**NotificationRequest**


## delete_notification

```python
None client.delete_notification(id: UUID)
```

**DELETE** `/api/notification/{id}`

Delete notification (deleteNotification)

Deletes notification by its id.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## delete_notification_request

```python
None client.delete_notification_request(id: UUID)
```

**DELETE** `/api/notification/request/{id}`

Delete notification request (deleteNotificationRequest)

Deletes notification request by its id.  If the request has status `SENT` - all sent notifications for this request will be deleted. If it is `SCHEDULED`, the request will be cancelled.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_available_delivery_methods

```python
List[NotificationDeliveryMethod] client.get_available_delivery_methods()
```

**GET** `/api/notification/deliveryMethods`

Get available delivery methods (getAvailableDeliveryMethods)

Returns the list of delivery methods that are properly configured and are allowed to be used for sending notifications.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.

### Return type

**List[NotificationDeliveryMethod]**


## get_notification_request_by_id

```python
NotificationRequestInfo client.get_notification_request_by_id(id: UUID)
```

**GET** `/api/notification/request/{id}`

Get notification request by id (getNotificationRequestById)

Fetches notification request info by request id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**NotificationRequestInfo**


## get_notification_request_preview

```python
NotificationRequestPreview client.get_notification_request_preview(notification_request: NotificationRequest, recipients_preview_size: Optional[int] = None)
```

**POST** `/api/notification/request/preview`

Get notification request preview (getNotificationRequestPreview)

Returns preview for notification request.  `processedTemplates` shows how the notifications for each delivery method will look like for the first recipient of the corresponding notification target.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **notification_request** | **NotificationRequest** |  | |
| **recipients_preview_size** | **int** | Amount of the recipients to show in preview | [optional] [default to 20] |

### Return type

**NotificationRequestPreview**


## get_notification_requests

```python
PageDataNotificationRequestInfo client.get_notification_requests(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/notification/requests`

Get notification requests (getNotificationRequests)

Returns the page of notification requests submitted by users of this tenant or sysadmins.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filed based on the used template name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataNotificationRequestInfo**


## get_notification_settings

```python
NotificationSettings client.get_notification_settings()
```

**GET** `/api/notification/settings`

Get notification settings (getNotificationSettings)

Retrieves notification settings for this tenant or sysadmin.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.

### Return type

**NotificationSettings**


## get_notifications

```python
PageDataNotification client.get_notifications(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, unread_only: Optional[bool] = None, delivery_method: Optional[str] = None)
```

**GET** `/api/notifications`

Get notifications (getNotifications)

Returns the page of notifications for current user.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for any authorized user.   **WebSocket API**:  There are 2 types of subscriptions: one for unread notifications count, another for unread notifications themselves.  The URI for opening WS session for notifications: `/api/ws/plugins/notifications`.  Subscription command for unread notifications count: ``` {   \"unreadCountSubCmd\": {     \"cmdId\": 1234   } } ``` To subscribe for latest unread notifications: ``` {   \"unreadSubCmd\": {     \"cmdId\": 1234,     \"limit\": 10   } } ``` To unsubscribe from any subscription: ``` {   \"unsubCmd\": {     \"cmdId\": 1234   } } ``` To mark certain notifications as read, use following command: ``` {   \"markAsReadCmd\": {     \"cmdId\": 1234,     \"notifications\": [       \"6f860330-7fc2-11ed-b855-7dd3b7d2faa9\",       \"5b6dfee0-8d0d-11ed-b61f-35a57b03dade\"     ]   } }  ``` To mark all notifications as read: ``` {   \"markAllAsReadCmd\": {     \"cmdId\": 1234   } } ```   Update structure for unread **notifications count subscription**: ``` {   \"cmdId\": 1234,   \"totalUnreadCount\": 55 } ``` For **notifications subscription**: - full update of latest unread notifications: ``` {   \"cmdId\": 1234,   \"notifications\": [     {       \"id\": {         \"entityType\": \"NOTIFICATION\",         \"id\": \"6f860330-7fc2-11ed-b855-7dd3b7d2faa9\"       },       ...     }   ],   \"totalUnreadCount\": 1 } ``` - when new notification arrives or shown notification is updated: ``` {   \"cmdId\": 1234,   \"update\": {     \"id\": {       \"entityType\": \"NOTIFICATION\",       \"id\": \"6f860330-7fc2-11ed-b855-7dd3b7d2faa9\"     },     # updated notification info, text, subject etc.     ...   },   \"totalUnreadCount\": 2 } ``` - when unread notifications count changes: ``` {   \"cmdId\": 1234,   \"totalUnreadCount\": 5 } ```


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on notification subject or text | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |
| **unread_only** | **bool** | To search for unread notifications only | [optional] [default to False] |
| **delivery_method** | **str** | Delivery method | [optional] [enum: WEB, MOBILE_APP] |

### Return type

**PageDataNotification**


## get_unread_notifications_count

```python
int client.get_unread_notifications_count(delivery_method: Optional[str] = None)
```

**GET** `/api/notifications/unread/count`

Get unread notifications count (getUnreadNotificationsCount)

Returns unread notifications count for chosen delivery method.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **delivery_method** | **str** | Delivery method | [optional] [enum: WEB, MOBILE_APP] |

### Return type

**int**


## get_user_notification_settings

```python
UserNotificationSettings client.get_user_notification_settings()
```

**GET** `/api/notification/settings/user`

getUserNotificationSettings

### Return type

**UserNotificationSettings**


## mark_all_notifications_as_read

```python
None client.mark_all_notifications_as_read(delivery_method: Optional[str] = None)
```

**PUT** `/api/notifications/read`

Mark all notifications as read (markAllNotificationsAsRead)

Marks all unread notifications as read.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **delivery_method** | **str** | Delivery method | [optional] [enum: WEB, MOBILE_APP] |

### Return type

None (empty response body)


## mark_notification_as_read

```python
None client.mark_notification_as_read(id: UUID)
```

**PUT** `/api/notification/{id}/read`

Mark notification as read (markNotificationAsRead)

Marks notification as read by its id.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## save_notification_settings

```python
NotificationSettings client.save_notification_settings(notification_settings: NotificationSettings)
```

**POST** `/api/notification/settings`

Save notification settings (saveNotificationSettings)

Saves notification settings for this tenant or sysadmin. `deliveryMethodsConfigs` of the settings must be specified.  Here is an example of the notification settings with Slack configuration: ```json {   \"deliveryMethodsConfigs\": {     \"SLACK\": {       \"method\": \"SLACK\",       \"botToken\": \"xoxb-....\"     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **notification_settings** | **NotificationSettings** |  | |

### Return type

**NotificationSettings**


## save_user_notification_settings

```python
UserNotificationSettings client.save_user_notification_settings(user_notification_settings: UserNotificationSettings)
```

**POST** `/api/notification/settings/user`

saveUserNotificationSettings


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_notification_settings** | **UserNotificationSettings** |  | |

### Return type

**UserNotificationSettings**


## send_addon_access_error

```python
None client.send_addon_access_error(addon_type: str)
```

**POST** `/api/notification/sendAddonAccessError/{addonType}`

Send add-on access error notification to System/Tenant administrators (sendAddonAccessError)

Send add-on access error notification by Tenant Administrator or Customer User to System/Tenant administrators.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **addon_type** | **str** | Addon type | [enum: EDGE, TRENDZ, WHITE_LABELING] |

### Return type

None (empty response body)


## send_entities_limit_increase_request

```python
None client.send_entities_limit_increase_request(entity_type: str)
```

**POST** `/api/notification/entitiesLimitIncreaseRequest/{entityType}`

Send entity limit increase request notification to System/Tenant administrators (sendEntitiesLimitIncreaseRequest)

Send entity limit increase request notification by Tenant Administrator or Customer User to System/Tenant administrators.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | Entity type | [enum: DEVICE, ASSET, CUSTOMER, USER, DASHBOARD, RULE_CHAIN, EDGE, INTEGRATION, CONVERTER, SCHEDULER_EVENT] |

### Return type

None (empty response body)

