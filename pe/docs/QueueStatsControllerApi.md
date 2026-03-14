# QueueStatsControllerApi

`ThingsboardClient` methods:

```python
QueueStats client.get_queue_stats_by_id(queue_stats_id: str)  # Get Queue stats entity by id (getQueueStatsById)
List[QueueStats] client.get_queue_stats_by_ids(queue_stats_ids: List[str])  # Get QueueStats By Ids (getQueueStatsByIds)
PageDataQueueStats client.get_tenant_queue_stats(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Queue Stats entities (getTenantQueueStats)
```


## get_queue_stats_by_id

```python
QueueStats client.get_queue_stats_by_id(queue_stats_id: str)
```

**GET** `/api/queueStats/{queueStatsId}`

Get Queue stats entity by id (getQueueStatsById)

Fetch the Queue stats object based on the provided Queue stats id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **queue_stats_id** | **str** | A string value representing the queue stats id. For example, '687f294c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**QueueStats**


## get_queue_stats_by_ids

```python
List[QueueStats] client.get_queue_stats_by_ids(queue_stats_ids: List[str])
```

**GET** `/api/queueStats/list`

Get QueueStats By Ids (getQueueStatsByIds)

Fetch the Queue stats objects based on the provided ids. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **queue_stats_ids** | **List[str]** | A list of queue stats ids, separated by comma ',' | |

### Return type

**List[QueueStats]**


## get_tenant_queue_stats

```python
PageDataQueueStats client.get_tenant_queue_stats(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/queueStats`

Get Queue Stats entities (getTenantQueueStats)

Returns a page of queue stats objects that are designed to collect queue statistics for every service. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the queue name or service id. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataQueueStats**

