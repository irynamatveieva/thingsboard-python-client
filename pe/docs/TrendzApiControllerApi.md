# TrendzApiControllerApi

`ThingsboardClient` methods:

```python
TrendzSummary client.get_trendz_summary()  # Get Trendz Summary (getTrendzSummary)
TrendzUsage client.get_trendz_usage()  # Get Trendz Usage (getTrendzUsage)
TrendzViewConfig client.get_trendz_view_by_id(view_id: str)  # Get Trendz View by Id (getTrendzViewById)
PageDataTrendzViewConfigLite client.get_trendz_views(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Trendz Views (getTrendzViews)
```


## get_trendz_summary

```python
TrendzSummary client.get_trendz_summary()
```

**GET** `/api/trendz/summary`

Get Trendz Summary (getTrendzSummary)

Fetch the Trendz summary object. Can only be used if Trendz is already synchronized and integration is enabled.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**TrendzSummary**


## get_trendz_usage

```python
TrendzUsage client.get_trendz_usage()
```

**GET** `/api/trendz/usage`

Get Trendz Usage (getTrendzUsage)

Fetch the Trendz usage object. Can only be used if Trendz is already synchronized and integration is enabled.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.

### Return type

**TrendzUsage**


## get_trendz_view_by_id

```python
TrendzViewConfig client.get_trendz_view_by_id(view_id: str)
```

**GET** `/api/trendz/view/{viewId}`

Get Trendz View by Id (getTrendzViewById)

Fetch the Trendz View object based on the provided Trendz View Id. Can only be used if Trendz is already synchronized and integration is enabled.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str** | A string value representing the Trendz view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TrendzViewConfig**


## get_trendz_views

```python
PageDataTrendzViewConfigLite client.get_trendz_views(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/trendz/view/all`

Get Trendz Views (getTrendzViews)

Returns a page of Trendz views that are available for the current user. Can only be used if Trendz is already synchronized and integration is enabled. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the Trendz view name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: name, createdAt, updatedAt, favorite] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataTrendzViewConfigLite**

