# WidgetTypeControllerApi

`ThingsboardClient` methods:

```python
None client.delete_widget_type(widget_type_id: str)  # Delete widget type (deleteWidgetType)
List[str] client.get_bundle_widget_type_fqns(widgets_bundle_id: str)  # Get all Widget type fqns for specified Bundle (getBundleWidgetTypeFqns)
List[WidgetType] client.get_bundle_widget_types(widgets_bundle_id: str)  # Get all Widget types for specified Bundle (getBundleWidgetTypes)
List[WidgetTypeDetails] client.get_bundle_widget_types_details(widgets_bundle_id: str, include_resources: Optional[bool] = None)  # Get all Widget types details for specified Bundle (getBundleWidgetTypesDetails)
PageDataWidgetTypeInfo client.get_bundle_widget_types_infos(widgets_bundle_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None, widget_type_list: Optional[List[str]] = None)  # Get Widget Type Info objects (getBundleWidgetTypesInfos)
WidgetType client.get_widget_type(fqn: str)  # Get Widget Type (getWidgetType)
WidgetTypeDetails client.get_widget_type_by_id(widget_type_id: str, include_resources: Optional[bool] = None)  # Get Widget Type Details (getWidgetTypeById)
WidgetTypeInfo client.get_widget_type_info_by_id(widget_type_id: str)  # Get Widget Type Info (getWidgetTypeInfoById)
PageDataWidgetTypeInfo client.get_widget_types(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, tenant_only: Optional[bool] = None, full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None, widget_type_list: Optional[List[str]] = None, scada_first: Optional[bool] = None)  # Get Widget Types (getWidgetTypes)
WidgetTypeDetails client.save_widget_type(widget_type_details: WidgetTypeDetails, update_existing_by_fqn: Optional[bool] = None)  # Create Or Update Widget Type (saveWidgetType)
```


## delete_widget_type

```python
None client.delete_widget_type(widget_type_id: str)
```

**DELETE** `/api/widgetType/{widgetTypeId}`

Delete widget type (deleteWidgetType)

Deletes the  Widget Type. Referencing non-existing Widget Type Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widget_type_id** | **str** | A string value representing the widget type id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_bundle_widget_type_fqns

```python
List[str] client.get_bundle_widget_type_fqns(widgets_bundle_id: str)
```

**GET** `/api/widgetTypeFqns`

Get all Widget type fqns for specified Bundle (getBundleWidgetTypeFqns)

Returns an array of Widget Type fqns that belong to specified Widget Bundle.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | Widget Bundle Id | |

### Return type

**List[str]**


## get_bundle_widget_types

```python
List[WidgetType] client.get_bundle_widget_types(widgets_bundle_id: str)
```

**GET** `/api/widgetsBundle/{widgetsBundleId}/widgetTypes`

Get all Widget types for specified Bundle (getBundleWidgetTypes)

Returns an array of Widget Type objects that belong to specified Widget Bundle.Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | Widget Bundle Id | |

### Return type

**List[WidgetType]**


## get_bundle_widget_types_details

```python
List[WidgetTypeDetails] client.get_bundle_widget_types_details(widgets_bundle_id: str, include_resources: Optional[bool] = None)
```

**GET** `/api/widgetTypesDetails`

Get all Widget types details for specified Bundle (getBundleWidgetTypesDetails)

Returns an array of Widget Type Details objects that belong to specified Widget Bundle.Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.    Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | Widget Bundle Id | |
| **include_resources** | **bool** | Export used resources and replace resource links with resource metadata | [optional] |

### Return type

**List[WidgetTypeDetails]**


## get_bundle_widget_types_infos

```python
PageDataWidgetTypeInfo client.get_bundle_widget_types_infos(widgets_bundle_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None, widget_type_list: Optional[List[str]] = None)
```

**GET** `/api/widgetTypesInfos`

Get Widget Type Info objects (getBundleWidgetTypesInfos)

Get the Widget Type Info objects based on the provided parameters. Widget Type Info is a lightweight object that represents Widget Type but does not contain the heavyweight widget descriptor JSON  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widgets_bundle_id** | **str** | Widget Bundle Id | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the widget type name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, deprecated, tenantId] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **full_search** | **bool** | Optional boolean parameter indicating whether search widgets by description not only by name | [optional] |
| **deprecated_filter** | **str** | Optional string parameter indicating whether to include deprecated widgets | [optional] [enum: ALL, ACTUAL, DEPRECATED] |
| **widget_type_list** | **List[str]** | A list of string values separated by comma ',' representing one of the widget type value | [optional] [enum: timeseries, latest, control, alarm, static] |

### Return type

**PageDataWidgetTypeInfo**


## get_widget_type

```python
WidgetType client.get_widget_type(fqn: str)
```

**GET** `/api/widgetType`

Get Widget Type (getWidgetType)

Get the Widget Type by FQN. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fqn** | **str** | Widget Type fqn | |

### Return type

**WidgetType**


## get_widget_type_by_id

```python
WidgetTypeDetails client.get_widget_type_by_id(widget_type_id: str, include_resources: Optional[bool] = None)
```

**GET** `/api/widgetType/{widgetTypeId}`

Get Widget Type Details (getWidgetTypeById)

Get the Widget Type Details based on the provided Widget Type Id. Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widget_type_id** | **str** | A string value representing the widget type id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **include_resources** | **bool** | Export used resources and replace resource links with resource metadata | [optional] |

### Return type

**WidgetTypeDetails**


## get_widget_type_info_by_id

```python
WidgetTypeInfo client.get_widget_type_info_by_id(widget_type_id: str)
```

**GET** `/api/widgetTypeInfo/{widgetTypeId}`

Get Widget Type Info (getWidgetTypeInfoById)

Get the Widget Type Info based on the provided Widget Type Id. Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widget_type_id** | **str** | A string value representing the widget type id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**WidgetTypeInfo**


## get_widget_types

```python
PageDataWidgetTypeInfo client.get_widget_types(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, tenant_only: Optional[bool] = None, full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None, widget_type_list: Optional[List[str]] = None, scada_first: Optional[bool] = None)
```

**GET** `/api/widgetTypes`

Get Widget Types (getWidgetTypes)

Returns a page of Widget Type objects available for current user. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the widget type name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, deprecated, tenantId] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **tenant_only** | **bool** | Optional boolean parameter indicating whether only tenant widget types should be returned | [optional] |
| **full_search** | **bool** | Optional boolean parameter indicating whether search widgets by description not only by name | [optional] |
| **deprecated_filter** | **str** | Optional string parameter indicating whether to include deprecated widgets | [optional] [enum: ALL, ACTUAL, DEPRECATED] |
| **widget_type_list** | **List[str]** | A list of string values separated by comma ',' representing one of the widget type value | [optional] [enum: timeseries, latest, control, alarm, static] |
| **scada_first** | **bool** | Optional boolean parameter indicating whether to fetch SCADA symbol widgets first | [optional] |

### Return type

**PageDataWidgetTypeInfo**


## save_widget_type

```python
WidgetTypeDetails client.save_widget_type(widget_type_details: WidgetTypeDetails, update_existing_by_fqn: Optional[bool] = None)
```

**POST** `/api/widgetType`

Create Or Update Widget Type (saveWidgetType)

Create or update the Widget Type. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory. When creating the Widget Type, platform generates Widget Type Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Type Id will be present in the response. Specify existing Widget Type id to update the Widget Type. Referencing non-existing Widget Type Id will cause 'Not Found' error.  Widget Type fqn is unique in the scope of System or Tenant. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create request is sent by user with 'SYS_ADMIN' authority.Remove 'id', 'tenantId' rom the request body example (below) to create new Widget Type entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **widget_type_details** | **WidgetTypeDetails** |  | |
| **update_existing_by_fqn** | **bool** | Optional boolean parameter indicating whether to update existing widget type by FQN if present instead of creating new one | [optional] |

### Return type

**WidgetTypeDetails**

