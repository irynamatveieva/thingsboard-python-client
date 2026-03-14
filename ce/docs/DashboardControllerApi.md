# DashboardControllerApi

`ThingsboardClient` methods:

```python
Dashboard client.add_dashboard_customers(dashboard_id: str, request_body: List[str])  # Adds the Dashboard Customers (addDashboardCustomers)
Dashboard client.assign_dashboard_to_customer(customer_id: str, dashboard_id: str)  # Assign the Dashboard (assignDashboardToCustomer)
Dashboard client.assign_dashboard_to_edge(edge_id: str, dashboard_id: str)  # Assign dashboard to edge (assignDashboardToEdge)
Dashboard client.assign_dashboard_to_public_customer(dashboard_id: str)  # Assign the Dashboard to Public Customer (assignDashboardToPublicCustomer)
None client.delete_dashboard(dashboard_id: str)  # Delete the Dashboard (deleteDashboard)
PageDataDashboardInfo client.get_customer_dashboards(customer_id: str, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Dashboards (getCustomerDashboards)
None client.get_dashboard_by_id(dashboard_id: str, include_resources: Optional[bool] = None, accept_encoding: Optional[str] = None)  # Get Dashboard (getDashboardById)
DashboardInfo client.get_dashboard_info_by_id(dashboard_id: str)  # Get Dashboard Info (getDashboardInfoById)
List[DashboardInfo] client.get_dashboards_by_ids(dashboard_ids: List[str])  # Get dashboards by Dashboard Ids (getDashboardsByIds)
PageDataDashboardInfo client.get_edge_dashboards(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Edge Dashboards (getEdgeDashboards)
None client.get_home_dashboard(accept_encoding: Optional[str] = None)  # Get Home Dashboard (getHomeDashboard)
HomeDashboardInfo client.get_home_dashboard_info()  # Get Home Dashboard Info (getHomeDashboardInfo)
int client.get_max_datapoints_limit()  # Get max data points limit (getMaxDatapointsLimit)
int client.get_server_time()  # Get server time (getServerTime)
PageDataDashboardInfo client.get_tenant_dashboards(page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Dashboards (getTenantDashboards)
PageDataDashboardInfo client.get_tenant_dashboards_by_tenant_id(tenant_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Dashboards by System Administrator (getTenantDashboardsByTenantId)
HomeDashboardInfo client.get_tenant_home_dashboard_info()  # Get Tenant Home Dashboard Info (getTenantHomeDashboardInfo)
Dashboard client.remove_dashboard_customers(dashboard_id: str, request_body: List[str])  # Remove the Dashboard Customers (removeDashboardCustomers)
Dashboard client.save_dashboard(dashboard: Dashboard, accept_encoding: Optional[str] = None)  # Create Or Update Dashboard (saveDashboard)
None client.set_tenant_home_dashboard_info(home_dashboard_info: HomeDashboardInfo)  # Update Tenant Home Dashboard Info (getTenantHomeDashboardInfo)
Dashboard client.unassign_dashboard_from_customer(customer_id: str, dashboard_id: str)  # Unassign the Dashboard (unassignDashboardFromCustomer)
Dashboard client.unassign_dashboard_from_edge(edge_id: str, dashboard_id: str)  # Unassign dashboard from edge (unassignDashboardFromEdge)
Dashboard client.unassign_dashboard_from_public_customer(dashboard_id: str)  # Unassign the Dashboard from Public Customer (unassignDashboardFromPublicCustomer)
Dashboard client.update_dashboard_customers(dashboard_id: str, request_body: Optional[List[str]] = None)  # Update the Dashboard Customers (updateDashboardCustomers)
```


## add_dashboard_customers

```python
Dashboard client.add_dashboard_customers(dashboard_id: str, request_body: List[str])
```

**POST** `/api/dashboard/{dashboardId}/customers/add`

Adds the Dashboard Customers (addDashboardCustomers)

Adds the list of Customers to the existing list of assignments for the Dashboard. Keeps previous assignments to customers that are not in the provided list. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | |

### Return type

**Dashboard**


## assign_dashboard_to_customer

```python
Dashboard client.assign_dashboard_to_customer(customer_id: str, dashboard_id: str)
```

**POST** `/api/customer/{customerId}/dashboard/{dashboardId}`

Assign the Dashboard (assignDashboardToCustomer)

Assign the Dashboard to specified Customer or do nothing if the Dashboard is already assigned to that Customer. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Dashboard**


## assign_dashboard_to_edge

```python
Dashboard client.assign_dashboard_to_edge(edge_id: str, dashboard_id: str)
```

**POST** `/api/edge/{edgeId}/dashboard/{dashboardId}`

Assign dashboard to edge (assignDashboardToEdge)

Creates assignment of an existing dashboard to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment dashboard (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once dashboard will be delivered to edge service, it's going to be available for usage on remote edge instance.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **dashboard_id** | **str** |  | |

### Return type

**Dashboard**


## assign_dashboard_to_public_customer

```python
Dashboard client.assign_dashboard_to_public_customer(dashboard_id: str)
```

**POST** `/api/customer/public/dashboard/{dashboardId}`

Assign the Dashboard to Public Customer (assignDashboardToPublicCustomer)

Assigns the dashboard to a special, auto-generated 'Public' Customer. Once assigned, unauthenticated users may browse the dashboard. This method is useful if you like to embed the dashboard on public web pages to be available for users that are not logged in. Be aware that making the dashboard public does not mean that it automatically makes all devices and assets you use in the dashboard to be public.Use [assign Asset to Public Customer](#!/asset-controller/assignAssetToPublicCustomerUsingPOST) and [assign Device to Public Customer](#!/device-controller/assignDeviceToPublicCustomerUsingPOST) for this purpose. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Dashboard**


## delete_dashboard

```python
None client.delete_dashboard(dashboard_id: str)
```

**DELETE** `/api/dashboard/{dashboardId}`

Delete the Dashboard (deleteDashboard)

Delete the Dashboard.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_customer_dashboards

```python
PageDataDashboardInfo client.get_customer_dashboards(customer_id: str, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/dashboards`

Get Customer Dashboards (getCustomerDashboards)

Returns a page of dashboard info objects owned by the specified customer. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **mobile** | **bool** | Exclude dashboards that are hidden for mobile | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_dashboard_by_id

```python
None client.get_dashboard_by_id(dashboard_id: str, include_resources: Optional[bool] = None, accept_encoding: Optional[str] = None)
```

**GET** `/api/dashboard/{dashboardId}`

Get Dashboard (getDashboardById)

Get the dashboard based on 'dashboardId' parameter. The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **include_resources** | **bool** | Export used resources and replace resource links with resource metadata | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

None (empty response body)


## get_dashboard_info_by_id

```python
DashboardInfo client.get_dashboard_info_by_id(dashboard_id: str)
```

**GET** `/api/dashboard/info/{dashboardId}`

Get Dashboard Info (getDashboardInfoById)

Get the information about the dashboard based on 'dashboardId' parameter. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**DashboardInfo**


## get_dashboards_by_ids

```python
List[DashboardInfo] client.get_dashboards_by_ids(dashboard_ids: List[str])
```

**GET** `/api/dashboards/list`

Get dashboards by Dashboard Ids (getDashboardsByIds)

Returns a list of DashboardInfo objects based on the provided ids.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_ids** | **List[str]** | A list of dashboard ids, separated by comma ',' | |

### Return type

**List[DashboardInfo]**


## get_edge_dashboards

```python
PageDataDashboardInfo client.get_edge_dashboards(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/edge/{edgeId}/dashboards`

Get Edge Dashboards (getEdgeDashboards)

Returns a page of dashboard info objects assigned to the specified edge. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_home_dashboard

```python
None client.get_home_dashboard(accept_encoding: Optional[str] = None)
```

**GET** `/api/dashboard/home`

Get Home Dashboard (getHomeDashboard)

Returns the home dashboard object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the User. If 'homeDashboardId' parameter is not set on the User level and the User has authority 'CUSTOMER_USER', check the same parameter for the corresponding Customer. If 'homeDashboardId' parameter is not set on the User and Customer levels then checks the same parameter for the Tenant that owns the user. The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accept_encoding** | **str** |  | [optional] |

### Return type

None (empty response body)


## get_home_dashboard_info

```python
HomeDashboardInfo client.get_home_dashboard_info()
```

**GET** `/api/dashboard/home/info`

Get Home Dashboard Info (getHomeDashboardInfo)

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the User. If 'homeDashboardId' parameter is not set on the User level and the User has authority 'CUSTOMER_USER', check the same parameter for the corresponding Customer. If 'homeDashboardId' parameter is not set on the User and Customer levels then checks the same parameter for the Tenant that owns the user.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**HomeDashboardInfo**


## get_max_datapoints_limit

```python
int client.get_max_datapoints_limit()
```

**GET** `/api/dashboard/maxDatapointsLimit`

Get max data points limit (getMaxDatapointsLimit)

Get the maximum number of data points that dashboard may request from the server per in a single subscription command. This value impacts the time window behavior. It impacts 'Max values' parameter in case user selects 'None' as 'Data aggregation function'. It also impacts the 'Grouping interval' in case of any other 'Data aggregation function' is selected. The actual value of the limit is configurable in the system configuration file.

### Return type

**int**


## get_server_time

```python
int client.get_server_time()
```

**GET** `/api/dashboard/serverTime`

Get server time (getServerTime)

Get the server time (milliseconds since January 1, 1970 UTC). Used to adjust view of the dashboards according to the difference between browser and server time.

### Return type

**int**


## get_tenant_dashboards

```python
PageDataDashboardInfo client.get_tenant_dashboards(page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/dashboards`

Get Tenant Dashboards (getTenantDashboards)

Returns a page of dashboard info objects owned by the tenant of a current user. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **mobile** | **bool** | Exclude dashboards that are hidden for mobile | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_tenant_dashboards_by_tenant_id

```python
PageDataDashboardInfo client.get_tenant_dashboards_by_tenant_id(tenant_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/{tenantId}/dashboards`

Get Tenant Dashboards by System Administrator (getTenantDashboardsByTenantId)

Returns a page of dashboard info objects owned by tenant. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_id** | **str** | A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_tenant_home_dashboard_info

```python
HomeDashboardInfo client.get_tenant_home_dashboard_info()
```

**GET** `/api/tenant/dashboard/home/info`

Get Tenant Home Dashboard Info (getTenantHomeDashboardInfo)

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the corresponding tenant.   Available for users with 'TENANT_ADMIN' authority.

### Return type

**HomeDashboardInfo**


## remove_dashboard_customers

```python
Dashboard client.remove_dashboard_customers(dashboard_id: str, request_body: List[str])
```

**POST** `/api/dashboard/{dashboardId}/customers/remove`

Remove the Dashboard Customers (removeDashboardCustomers)

Removes the list of Customers from the existing list of assignments for the Dashboard. Keeps other assignments to customers that are not in the provided list. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | |

### Return type

**Dashboard**


## save_dashboard

```python
Dashboard client.save_dashboard(dashboard: Dashboard, accept_encoding: Optional[str] = None)
```

**POST** `/api/dashboard`

Create Or Update Dashboard (saveDashboard)

Create or update the Dashboard. When creating dashboard, platform generates Dashboard Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Dashboard id will be present in the response. Specify existing Dashboard id to update the dashboard. Referencing non-existing dashboard Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Dashboard entity.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard** | **Dashboard** | A JSON value representing the dashboard. | |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**Dashboard**


## set_tenant_home_dashboard_info

```python
None client.set_tenant_home_dashboard_info(home_dashboard_info: HomeDashboardInfo)
```

**POST** `/api/tenant/dashboard/home/info`

Update Tenant Home Dashboard Info (getTenantHomeDashboardInfo)

Update the home dashboard assignment for the current tenant.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **home_dashboard_info** | **HomeDashboardInfo** |  | |

### Return type

None (empty response body)


## unassign_dashboard_from_customer

```python
Dashboard client.unassign_dashboard_from_customer(customer_id: str, dashboard_id: str)
```

**DELETE** `/api/customer/{customerId}/dashboard/{dashboardId}`

Unassign the Dashboard (unassignDashboardFromCustomer)

Unassign the Dashboard from specified Customer or do nothing if the Dashboard is already assigned to that Customer. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Dashboard**


## unassign_dashboard_from_edge

```python
Dashboard client.unassign_dashboard_from_edge(edge_id: str, dashboard_id: str)
```

**DELETE** `/api/edge/{edgeId}/dashboard/{dashboardId}`

Unassign dashboard from edge (unassignDashboardFromEdge)

Clears assignment of the dashboard to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove dashboard (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove dashboard locally.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **dashboard_id** | **str** |  | |

### Return type

**Dashboard**


## unassign_dashboard_from_public_customer

```python
Dashboard client.unassign_dashboard_from_public_customer(dashboard_id: str)
```

**DELETE** `/api/customer/public/dashboard/{dashboardId}`

Unassign the Dashboard from Public Customer (unassignDashboardFromPublicCustomer)

Unassigns the dashboard from a special, auto-generated 'Public' Customer. Once unassigned, unauthenticated users may no longer browse the dashboard. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Dashboard**


## update_dashboard_customers

```python
Dashboard client.update_dashboard_customers(dashboard_id: str, request_body: Optional[List[str]] = None)
```

**POST** `/api/dashboard/{dashboardId}/customers`

Update the Dashboard Customers (updateDashboardCustomers)

Updates the list of Customers that this Dashboard is assigned to. Removes previous assignments to customers that are not in the provided list. Returns the Dashboard object.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | [optional] |

### Return type

**Dashboard**

