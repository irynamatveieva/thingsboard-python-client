# NotificationRuleControllerApi

`ThingsboardClient` methods:

```python
None client.delete_notification_rule(id: UUID)  # Delete notification rule (deleteNotificationRule)
NotificationRuleInfo client.get_notification_rule_by_id(id: UUID)  # Get notification rule by id (getNotificationRuleById)
PageDataNotificationRuleInfo client.get_notification_rules(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get notification rules (getNotificationRules)
NotificationRule client.save_notification_rule(notification_rule: NotificationRule)  # Save notification rule (saveNotificationRule)
```


## delete_notification_rule

```python
None client.delete_notification_rule(id: UUID)
```

**DELETE** `/api/notification/rule/{id}`

Delete notification rule (deleteNotificationRule)

Deletes notification rule by id. Cancels all related scheduled notification requests (e.g. due to escalation table)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_notification_rule_by_id

```python
NotificationRuleInfo client.get_notification_rule_by_id(id: UUID)
```

**GET** `/api/notification/rule/{id}`

Get notification rule by id (getNotificationRuleById)

Fetches notification rule info by rule's id. In addition to regular notification rule fields, there are `templateName` and `deliveryMethods` in the response.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**NotificationRuleInfo**


## get_notification_rules

```python
PageDataNotificationRuleInfo client.get_notification_rules(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/notification/rules`

Get notification rules (getNotificationRules)

Returns the page of notification rules.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on rule's name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataNotificationRuleInfo**


## save_notification_rule

```python
NotificationRule client.save_notification_rule(notification_rule: NotificationRule)
```

**POST** `/api/notification/rule`

Save notification rule (saveNotificationRule)

Creates or updates notification rule.   Mandatory properties are `name`, `templateId` (of a template with `notificationType` matching to rule's `triggerType`), `triggerType`, `triggerConfig` and `recipientConfig`. Additionally, you may specify rule `description` inside of `additionalConfig`.  Trigger type of the rule cannot be changed. Available trigger types for tenant: `ENTITY_ACTION`, `ALARM`, `ALARM_COMMENT`, `ALARM_ASSIGNMENT`, `DEVICE_ACTIVITY`, `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`. For sysadmin, there are following trigger types available: `ENTITIES_LIMIT`, `API_USAGE_LIMIT`, `NEW_PLATFORM_VERSION`.  Here is an example of notification rule to send notification when a device, asset or customer is created or deleted: ```json {   \"name\": \"Entity action\",   \"templateId\": {     \"entityType\": \"NOTIFICATION_TEMPLATE\",     \"id\": \"32117320-d785-11ed-a06c-21dd57dd88ca\"   },   \"triggerType\": \"ENTITY_ACTION\",   \"triggerConfig\": {     \"entityTypes\": [       \"CUSTOMER\",       \"DEVICE\",       \"ASSET\"     ],     \"created\": true,     \"updated\": false,     \"deleted\": true,     \"triggerType\": \"ENTITY_ACTION\"   },   \"recipientsConfig\": {     \"targets\": [       \"320f2930-d785-11ed-a06c-21dd57dd88ca\"     ],     \"triggerType\": \"ENTITY_ACTION\"   },   \"additionalConfig\": {     \"description\": \"Send notification to tenant admins or customer users when a device, asset or customer is created\"   },   \"templateName\": \"Entity action notification\",   \"deliveryMethods\": [     \"WEB\"   ] } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **notification_rule** | **NotificationRule** |  | |

### Return type

**NotificationRule**

