# EntityViewControllerApi

`ThingsboardClient` methods:

```python
EntityView client.assign_entity_view_to_customer(customer_id: str, entity_view_id: str)  # Assign Entity View to customer (assignEntityViewToCustomer)
EntityView client.assign_entity_view_to_edge(edge_id: str, entity_view_id: str)  # Assign entity view to edge (assignEntityViewToEdge)
EntityView client.assign_entity_view_to_public_customer(entity_view_id: str)  # Make entity view publicly available (assignEntityViewToPublicCustomer)
None client.delete_entity_view(entity_view_id: str)  # Delete entity view (deleteEntityView)
List[EntityView] client.find_entity_views_by_query(entity_view_search_query: EntityViewSearchQuery)  # Find related entity views (findEntityViewsByQuery)
PageDataEntityViewInfo client.get_customer_entity_view_infos(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Entity View info (getCustomerEntityViewInfos)
PageDataEntityView client.get_customer_entity_views(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Entity Views (getCustomerEntityViews)
PageDataEntityView client.get_edge_entity_views(edge_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)  # getEdgeEntityViews
EntityView client.get_entity_view_by_id(entity_view_id: str)  # Get entity view (getEntityViewById)
EntityViewInfo client.get_entity_view_info_by_id(entity_view_id: str)  # Get Entity View info (getEntityViewInfoById)
List[EntitySubtype] client.get_entity_view_types()  # Get Entity View Types (getEntityViewTypes)
List[EntityView] client.get_entity_views_by_ids(entity_view_ids: List[str])  # Get Entity Views By Ids (getEntityViewsByIds)
EntityView client.get_tenant_entity_view_by_name(entity_view_name: str)  # Get Entity View by name (getTenantEntityViewByName)
PageDataEntityViewInfo client.get_tenant_entity_view_infos(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Entity Views (getTenantEntityViews)
PageDataEntityView client.get_tenant_entity_views(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Entity Views (getTenantEntityViews)
EntityView client.save_entity_view(entity_view: EntityView, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)  # Save or update entity view (saveEntityView)
EntityView client.unassign_entity_view_from_customer(entity_view_id: str)  # Unassign Entity View from customer (unassignEntityViewFromCustomer)
EntityView client.unassign_entity_view_from_edge(edge_id: str, entity_view_id: str)  # Unassign entity view from edge (unassignEntityViewFromEdge)
```


## assign_entity_view_to_customer

```python
EntityView client.assign_entity_view_to_customer(customer_id: str, entity_view_id: str)
```

**POST** `/api/customer/{customerId}/entityView/{entityViewId}`

Assign Entity View to customer (assignEntityViewToCustomer)

Creates assignment of the Entity View to customer. Customer will be able to query Entity View afterwards.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **entity_view_id** | **str** | A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityView**


## assign_entity_view_to_edge

```python
EntityView client.assign_entity_view_to_edge(edge_id: str, entity_view_id: str)
```

**POST** `/api/edge/{edgeId}/entityView/{entityViewId}`

Assign entity view to edge (assignEntityViewToEdge)

Creates assignment of an existing entity view to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment entity view (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once entity view will be delivered to edge service, it's going to be available for usage on remote edge instance.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **entity_view_id** | **str** |  | |

### Return type

**EntityView**


## assign_entity_view_to_public_customer

```python
EntityView client.assign_entity_view_to_public_customer(entity_view_id: str)
```

**POST** `/api/customer/public/entityView/{entityViewId}`

Make entity view publicly available (assignEntityViewToPublicCustomer)

Entity View will be available for non-authorized (not logged-in) users. This is useful to create dashboards that you plan to share/embed on a publicly available website. However, users that are logged-in and belong to different tenant will not be able to access the entity view.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_id** | **str** | A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityView**


## delete_entity_view

```python
None client.delete_entity_view(entity_view_id: str)
```

**DELETE** `/api/entityView/{entityViewId}`

Delete entity view (deleteEntityView)

Delete the EntityView object based on the provided entity view id.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_id** | **str** | A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## find_entity_views_by_query

```python
List[EntityView] client.find_entity_views_by_query(entity_view_search_query: EntityViewSearchQuery)
```

**POST** `/api/entityViews`

Find related entity views (findEntityViewsByQuery)

Returns all entity views that are related to the specific entity. The entity id, relation type, entity view types, depth of the search, and other query parameters defined using complex 'EntityViewSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_search_query** | **EntityViewSearchQuery** |  | |

### Return type

**List[EntityView]**


## get_customer_entity_view_infos

```python
PageDataEntityViewInfo client.get_customer_entity_view_infos(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/entityViewInfos`

Get Customer Entity View info (getCustomerEntityViewInfos)

Returns a page of Entity View info objects assigned to customer. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** |   ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   \"type\": \"entityViewType\",   \"entityViewType\": \"Concrete Mixer\",   \"entityViewNameFilter\": \"CAT\" } ``` | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the entity view name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityViewInfo**


## get_customer_entity_views

```python
PageDataEntityView client.get_customer_entity_views(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/entityViews`

Get Customer Entity Views (getCustomerEntityViews)

Returns a page of Entity View objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** |   ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   \"type\": \"entityViewType\",   \"entityViewType\": \"Concrete Mixer\",   \"entityViewNameFilter\": \"CAT\" } ``` | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the entity view name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityView**


## get_edge_entity_views

```python
PageDataEntityView client.get_edge_entity_views(edge_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)
```

**GET** `/api/edge/{edgeId}/entityViews`

getEdgeEntityViews


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **page_size** | **int** |  | |
| **page** | **int** |  | |
| **type** | **str** |  | [optional] |
| **text_search** | **str** |  | [optional] |
| **sort_property** | **str** |  | [optional] |
| **sort_order** | **str** |  | [optional] |
| **start_time** | **int** |  | [optional] |
| **end_time** | **int** |  | [optional] |

### Return type

**PageDataEntityView**


## get_entity_view_by_id

```python
EntityView client.get_entity_view_by_id(entity_view_id: str)
```

**GET** `/api/entityView/{entityViewId}`

Get entity view (getEntityViewById)

Fetch the EntityView object based on the provided entity view id. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_id** | **str** | A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityView**


## get_entity_view_info_by_id

```python
EntityViewInfo client.get_entity_view_info_by_id(entity_view_id: str)
```

**GET** `/api/entityView/info/{entityViewId}`

Get Entity View info (getEntityViewInfoById)

Fetch the Entity View info object based on the provided Entity View Id. Entity Views Info extends the Entity View with customer title and 'is public' flag. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_id** | **str** | A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityViewInfo**


## get_entity_view_types

```python
List[EntitySubtype] client.get_entity_view_types()
```

**GET** `/api/entityView/types`

Get Entity View Types (getEntityViewTypes)

Returns a set of unique entity view types based on entity views that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**List[EntitySubtype]**


## get_entity_views_by_ids

```python
List[EntityView] client.get_entity_views_by_ids(entity_view_ids: List[str])
```

**GET** `/api/entityViews/list`

Get Entity Views By Ids (getEntityViewsByIds)

Requested entity views must be owned by tenant or assigned to customer which user is performing the request. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_ids** | **List[str]** | A list of entity view ids, separated by comma ',' | |

### Return type

**List[EntityView]**


## get_tenant_entity_view_by_name

```python
EntityView client.get_tenant_entity_view_by_name(entity_view_name: str)
```

**GET** `/api/tenant/entityView`

Get Entity View by name (getTenantEntityViewByName)

Fetch the Entity View object based on the tenant id and entity view name.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_name** | **str** | Entity View name | |

### Return type

**EntityView**


## get_tenant_entity_view_infos

```python
PageDataEntityViewInfo client.get_tenant_entity_view_infos(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/entityViewInfos`

Get Tenant Entity Views (getTenantEntityViews)

Returns a page of entity views info owned by tenant. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** |   ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   \"type\": \"entityViewType\",   \"entityViewType\": \"Concrete Mixer\",   \"entityViewNameFilter\": \"CAT\" } ``` | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the entity view name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityViewInfo**


## get_tenant_entity_views

```python
PageDataEntityView client.get_tenant_entity_views(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/entityViews`

Get Tenant Entity Views (getTenantEntityViews)

Returns a page of entity views owned by tenant. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** |   ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   \"type\": \"entityViewType\",   \"entityViewType\": \"Concrete Mixer\",   \"entityViewNameFilter\": \"CAT\" } ``` | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the entity view name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityView**


## save_entity_view

```python
EntityView client.save_entity_view(entity_view: EntityView, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)
```

**POST** `/api/entityView`

Save or update entity view (saveEntityView)

Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Entity View entity.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view** | **EntityView** |  | |
| **name_conflict_policy** | **NameConflictPolicy** | Optional value of name conflict policy. Possible values: FAIL or UNIQUIFY.  If omitted, FAIL policy is applied. FAIL policy implies exception will be thrown if an entity with the same name already exists.  UNIQUIFY policy appends a suffix to the entity name, if a name conflict occurs. | [optional] [enum: FAIL, UNIQUIFY] |
| **uniquify_separator** | **str** | Optional value of name suffix separator used by UNIQUIFY policy. By default, underscore separator is used. For example, strategy is UNIQUIFY, separator is '-'; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-7fsh4f'. | [optional] [default to &#39;_&#39;] |
| **uniquify_strategy** | **UniquifyStrategy** | Optional value of uniquify strategy used by UNIQUIFY policy. Possible values: RANDOM or INCREMENTAL. By default, RANDOM strategy is used, which means random alphanumeric string will be added as a suffix to entity name. INCREMENTAL implies the first possible number starting from 1 will be added as a name suffix. For example, strategy is UNIQUIFY, uniquify strategy is INCREMENTAL; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-1. | [optional] [enum: RANDOM, INCREMENTAL] |

### Return type

**EntityView**


## unassign_entity_view_from_customer

```python
EntityView client.unassign_entity_view_from_customer(entity_view_id: str)
```

**DELETE** `/api/customer/entityView/{entityViewId}`

Unassign Entity View from customer (unassignEntityViewFromCustomer)

Clears assignment of the Entity View to customer. Customer will not be able to query Entity View afterwards.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_view_id** | **str** | A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityView**


## unassign_entity_view_from_edge

```python
EntityView client.unassign_entity_view_from_edge(edge_id: str, entity_view_id: str)
```

**DELETE** `/api/edge/{edgeId}/entityView/{entityViewId}`

Unassign entity view from edge (unassignEntityViewFromEdge)

Clears assignment of the entity view to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove entity view (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove entity view locally.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **entity_view_id** | **str** |  | |

### Return type

**EntityView**

