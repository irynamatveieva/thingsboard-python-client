# JobControllerApi

`ThingsboardClient` methods:

```python
None client.cancel_job(id: UUID)  # cancelJob
None client.delete_job(id: UUID)  # deleteJob
Job client.get_job_by_id(id: UUID)  # getJobById
PageDataJob client.get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, types: Optional[List[JobType]] = None, statuses: Optional[List[JobStatus]] = None, entities: Optional[List[UUID]] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)  # getJobs
None client.reprocess_job(id: UUID)  # reprocessJob
```


## cancel_job

```python
None client.cancel_job(id: UUID)
```

**POST** `/api/job/{id}/cancel`

cancelJob


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## delete_job

```python
None client.delete_job(id: UUID)
```

**DELETE** `/api/job/{id}`

deleteJob


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_job_by_id

```python
Job client.get_job_by_id(id: UUID)
```

**GET** `/api/job/{id}`

getJobById


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**Job**


## get_jobs

```python
PageDataJob client.get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, types: Optional[List[JobType]] = None, statuses: Optional[List[JobStatus]] = None, entities: Optional[List[UUID]] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)
```

**GET** `/api/jobs`

getJobs


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on job's description | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |
| **types** | **List[JobType]** |  | [optional] |
| **statuses** | **List[JobStatus]** |  | [optional] |
| **entities** | **List[UUID]** |  | [optional] |
| **start_time** | **int** |  | [optional] |
| **end_time** | **int** |  | [optional] |

### Return type

**PageDataJob**


## reprocess_job

```python
None client.reprocess_job(id: UUID)
```

**POST** `/api/job/{id}/reprocess`

reprocessJob


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)

