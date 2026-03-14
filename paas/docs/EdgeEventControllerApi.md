# EdgeEventControllerApi

`ThingsboardClient` methods:

```python
PageDataEdgeEvent client.get_edge_events(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)  # Get Edge Events (getEdgeEvents)
```


## get_edge_events

```python
PageDataEdgeEvent client.get_edge_events(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)
```

**GET** `/api/edge/{edgeId}/events`

Get Edge Events (getEdgeEvents)

Returns a page of edge events for the requested edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge event type name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | Timestamp. Edge events with creation time before it won't be queried | [optional] |
| **end_time** | **int** | Timestamp. Edge events with creation time after it won't be queried | [optional] |

### Return type

**PageDataEdgeEvent**

