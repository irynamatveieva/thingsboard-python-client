# NotificationTemplateControllerApi

`ThingsboardClient` methods:

```python
None client.delete_notification_template_by_id(id: UUID)  # Delete notification template by id (deleteNotificationTemplateById
NotificationTemplate client.get_notification_template_by_id(id: UUID)  # Get notification template by id (getNotificationTemplateById)
PageDataNotificationTemplate client.get_notification_templates(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, notification_types: Optional[List[str]] = None)  # Get notification templates (getNotificationTemplates)
List[SlackConversation] client.list_slack_conversations(type: SlackConversationType, token: Optional[str] = None)  # List Slack conversations (listSlackConversations)
NotificationTemplate client.save_notification_template(notification_template: NotificationTemplate)  # Save notification template (saveNotificationTemplate)
```


## delete_notification_template_by_id

```python
None client.delete_notification_template_by_id(id: UUID)
```

**DELETE** `/api/notification/template/{id}`

Delete notification template by id (deleteNotificationTemplateById

Deletes notification template by its id.  This template cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_notification_template_by_id

```python
NotificationTemplate client.get_notification_template_by_id(id: UUID)
```

**GET** `/api/notification/template/{id}`

Get notification template by id (getNotificationTemplateById)

Fetches notification template by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**NotificationTemplate**


## get_notification_templates

```python
PageDataNotificationTemplate client.get_notification_templates(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, notification_types: Optional[List[str]] = None)
```

**GET** `/api/notification/templates`

Get notification templates (getNotificationTemplates)

Returns the page of notification templates owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on template's name and notification type | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |
| **notification_types** | **List[str]** | Comma-separated list of notification types to filter the templates | [optional] |

### Return type

**PageDataNotificationTemplate**


## list_slack_conversations

```python
List[SlackConversation] client.list_slack_conversations(type: SlackConversationType, token: Optional[str] = None)
```

**GET** `/api/notification/slack/conversations`

List Slack conversations (listSlackConversations)

List available Slack conversations by type.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **SlackConversationType** |  | [enum: DIRECT, PUBLIC_CHANNEL, PRIVATE_CHANNEL] |
| **token** | **str** | Slack bot token. If absent - system Slack settings will be used | [optional] |

### Return type

**List[SlackConversation]**


## save_notification_template

```python
NotificationTemplate client.save_notification_template(notification_template: NotificationTemplate)
```

**POST** `/api/notification/template`

Save notification template (saveNotificationTemplate)

Creates or updates notification template.  Here is an example of template to send notification via Web, SMS and Slack: ```json {   \"name\": \"Greetings\",   \"notificationType\": \"GENERAL\",   \"configuration\": {     \"deliveryMethodsTemplates\": {       \"WEB\": {         \"enabled\": true,         \"subject\": \"Greetings\",         \"body\": \"Hi there, ${recipientTitle}\",         \"additionalConfig\": {           \"icon\": {             \"enabled\": true,             \"icon\": \"back_hand\",             \"color\": \"#757575\"           },           \"actionButtonConfig\": {             \"enabled\": false           }         },         \"method\": \"WEB\"       },       \"SMS\": {         \"enabled\": true,         \"body\": \"Hi there, ${recipientTitle}\",         \"method\": \"SMS\"       },       \"SLACK\": {         \"enabled\": true,         \"body\": \"Hi there, @${recipientTitle}\",         \"method\": \"SLACK\"       }     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **notification_template** | **NotificationTemplate** |  | |

### Return type

**NotificationTemplate**

