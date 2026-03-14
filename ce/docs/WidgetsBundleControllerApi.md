# WidgetsBundleControllerApi

`ThingsboardClient` methods:

```python
None client.delete_widgets_bundle(widgets_bundle_id: str)  # Delete widgets bundle (deleteWidgetsBundle)
List[WidgetsBundle] client.get_all_widgets_bundles()  # Get all Widget Bundles (getAllWidgetsBundles)
WidgetsBundle client.get_widgets_bundle_by_id(widgets_bundle_id: str, inline_images: Optional[bool] = None)  # Get Widget Bundle (getWidgetsBundleById)
PageDataWidgetsBundle client.get_widgets_bundles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, tenant_only: Optional[bool] = None, full_search: Optional[bool] = None, scada_first: Optional[bool] = None)  # Get Widget Bundles (getWidgetsBundles)
List[WidgetsBundle] client.get_widgets_bundles_list(widgets_bundle_ids: List[str])  # Get Widgets Bundles By Ids (getWidgetsBundlesList)
WidgetsBundle client.save_widgets_bundle(widgets_bundle: WidgetsBundle)  # Create Or Update Widget Bundle (saveWidgetsBundle)
None client.update_widgets_bundle_widget_fqns(widgets_bundle_id: str, request_body: List[str])  # Update widgets bundle widgets list from widget type FQNs list (updateWidgetsBundleWidgetFqns)
None client.update_widgets_bundle_widget_types(widgets_bundle_id: str, request_body: List[str])  # Update widgets bundle widgets types list (updateWidgetsBundleWidgetTypes)
```


## delete_widgets_bundle

```python
None client.delete_widgets_bundle(widgets_bundle_id: str)
```

**DELETE** `/api/widgetsBundle/{widgetsBundleId}`

Delete widgets bundle (deleteWidgetsBundle)

Deletes the widget bundle. Referencing non-existing Widget Bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_all_widgets_bundles

```python
List[WidgetsBundle] client.get_all_widgets_bundles()
```

**GET** `/api/widgetsBundles/all`

Get all Widget Bundles (getAllWidgetsBundles)

Returns an array of Widget Bundle objects that are available for current user.Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.    Available for any authorized user. 

### Return type

**List[WidgetsBundle]**


## get_widgets_bundle_by_id

```python
WidgetsBundle client.get_widgets_bundle_by_id(widgets_bundle_id: str, inline_images: Optional[bool] = None)
```

**GET** `/api/widgetsBundle/{widgetsBundleId}`

Get Widget Bundle (getWidgetsBundleById)

Get the Widget Bundle based on the provided Widget Bundle Id. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.   Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **inline_images** | **bool** | Inline images as a data URL (Base64) | [optional] |

### Return type

**WidgetsBundle**


## get_widgets_bundles

```python
PageDataWidgetsBundle client.get_widgets_bundles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, tenant_only: Optional[bool] = None, full_search: Optional[bool] = None, scada_first: Optional[bool] = None)
```

**GET** `/api/widgetsBundles`

Get Widget Bundles (getWidgetsBundles)

Returns a page of Widget Bundle objects available for current user. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the widget bundle title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, tenantId] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **tenant_only** | **bool** | Optional boolean parameter to include only tenant-level bundles without system | [optional] |
| **full_search** | **bool** | Optional boolean parameter indicating extended search of widget bundles by description and by name / description of related widget types | [optional] |
| **scada_first** | **bool** | Optional boolean parameter indicating whether to fetch widgets bundles with SCADA symbols first. Works only when fullSearch parameter is enabled | [optional] |

### Return type

**PageDataWidgetsBundle**


## get_widgets_bundles_list

```python
List[WidgetsBundle] client.get_widgets_bundles_list(widgets_bundle_ids: List[str])
```

**GET** `/api/widgetsBundles/list`

Get Widgets Bundles By Ids (getWidgetsBundlesList)

Requested widgets bundles must be system level or owned by tenant of the user which is performing the request.   


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_ids** | **List[str]** | A list of widgets bundle ids, separated by comma ',' | |

### Return type

**List[WidgetsBundle]**


## save_widgets_bundle

```python
WidgetsBundle client.save_widgets_bundle(widgets_bundle: WidgetsBundle)
```

**POST** `/api/widgetsBundle`

Create Or Update Widget Bundle (saveWidgetsBundle)

Create or update the Widget Bundle. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  When creating the bundle, platform generates Widget Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Bundle Id will be present in the response. Specify existing Widget Bundle id to update the Widget Bundle. Referencing non-existing Widget Bundle Id will cause 'Not Found' error.  Widget Bundle alias is unique in the scope of tenant. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create bundle request is sent by user with 'SYS_ADMIN' authority.Remove 'id', 'tenantId' from the request body example (below) to create new Widgets Bundle entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle** | **WidgetsBundle** |  | |

### Return type

**WidgetsBundle**


## update_widgets_bundle_widget_fqns

```python
None client.update_widgets_bundle_widget_fqns(widgets_bundle_id: str, request_body: List[str])
```

**POST** `/api/widgetsBundle/{widgetsBundleId}/widgetTypeFqns`

Update widgets bundle widgets list from widget type FQNs list (updateWidgetsBundleWidgetFqns)

Updates widgets bundle widgets list from widget type FQNs list.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | |

### Return type

None (empty response body)


## update_widgets_bundle_widget_types

```python
None client.update_widgets_bundle_widget_types(widgets_bundle_id: str, request_body: List[str])
```

**POST** `/api/widgetsBundle/{widgetsBundleId}/widgetTypes`

Update widgets bundle widgets types list (updateWidgetsBundleWidgetTypes)

Updates widgets bundle widgets list.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | |

### Return type

None (empty response body)

