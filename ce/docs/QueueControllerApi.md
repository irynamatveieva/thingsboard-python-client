# QueueControllerApi

`ThingsboardClient` methods:

```python
None client.delete_queue(queue_id: str)  # Delete Queue (deleteQueue)
Queue client.get_queue_by_id(queue_id: str)  # Get Queue (getQueueById)
Queue client.get_queue_by_name(queue_name: str)  # Get Queue (getQueueByName)
PageDataQueue client.get_tenant_queues_by_service_type(service_type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Queues (getTenantQueuesByServiceType)
Queue client.save_queue(service_type: str, queue: Queue)  # Create Or Update Queue (saveQueue)
```


## delete_queue

```python
None client.delete_queue(queue_id: str)
```

**DELETE** `/api/queues/{queueId}`

Delete Queue (deleteQueue)

Deletes the Queue.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str** | A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_queue_by_id

```python
Queue client.get_queue_by_id(queue_id: str)
```

**GET** `/api/queues/{queueId}`

Get Queue (getQueueById)

Fetch the Queue object based on the provided Queue Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str** | A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Queue**


## get_queue_by_name

```python
Queue client.get_queue_by_name(queue_name: str)
```

**GET** `/api/queues/name/{queueName}`

Get Queue (getQueueByName)

Fetch the Queue object based on the provided Queue name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **queue_name** | **str** | A string value representing the queue id. For example, 'Main' | |

### Return type

**Queue**


## get_tenant_queues_by_service_type

```python
PageDataQueue client.get_tenant_queues_by_service_type(service_type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/queues`

Get Queues (getTenantQueuesByServiceType)

Returns a page of queues registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **service_type** | **str** | Service type (implemented only for the TB-RULE-ENGINE) | [enum: TB-RULE-ENGINE, TB-CORE, TB-TRANSPORT, JS-EXECUTOR] |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the queue name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, topic] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataQueue**


## save_queue

```python
Queue client.save_queue(service_type: str, queue: Queue)
```

**POST** `/api/queues`

Create Or Update Queue (saveQueue)

Create or update the Queue. When creating queue, platform generates Queue Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Specify existing Queue id to update the queue. Referencing non-existing Queue Id will cause 'Not Found' error.  Queue name is unique in the scope of sysadmin. Remove 'id', 'tenantId' from the request body example (below) to create new Queue entity.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **service_type** | **str** | Service type (implemented only for the TB-RULE-ENGINE) | [enum: TB-RULE-ENGINE, TB-CORE, TB-TRANSPORT, JS-EXECUTOR] |
| **queue** | **Queue** |  | |

### Return type

**Queue**

