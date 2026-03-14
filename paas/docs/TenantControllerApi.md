# TenantControllerApi

`ThingsboardClient` methods:

```python
None client.delete_tenant(tenant_id: str)  # Delete Tenant (deleteTenant)
Tenant client.get_tenant_by_id(tenant_id: str)  # Get Tenant (getTenantById)
TenantInfo client.get_tenant_info_by_id(tenant_id: str)  # Get Tenant Info (getTenantInfoById)
PageDataTenantInfo client.get_tenant_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenants Info (getTenants)
PageDataTenant client.get_tenants(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenants (getTenants)
List[Tenant] client.get_tenants_by_ids(tenant_ids: List[str])  # Get Tenants By Ids (getTenantsByIds)
Tenant client.save_tenant(tenant: Tenant)  # Create Or update Tenant (saveTenant)
```


## delete_tenant

```python
None client.delete_tenant(tenant_id: str)
```

**DELETE** `/api/tenant/{tenantId}`

Delete Tenant (deleteTenant)

Deletes the tenant, it's customers, rule chains, devices and all other related entities. Referencing non-existing tenant Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_id** | **str** | A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_tenant_by_id

```python
Tenant client.get_tenant_by_id(tenant_id: str)
```

**GET** `/api/tenant/{tenantId}`

Get Tenant (getTenantById)

Fetch the Tenant object based on the provided Tenant Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_id** | **str** | A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Tenant**


## get_tenant_info_by_id

```python
TenantInfo client.get_tenant_info_by_id(tenant_id: str)
```

**GET** `/api/tenant/info/{tenantId}`

Get Tenant Info (getTenantInfoById)

Fetch the Tenant Info object based on the provided Tenant Id. The Tenant Info object extends regular Tenant object and includes Tenant Profile name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_id** | **str** | A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TenantInfo**


## get_tenant_infos

```python
PageDataTenantInfo client.get_tenant_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenantInfos`

Get Tenants Info (getTenants)

Returns a page of tenant info objects registered in the platform. The Tenant Info object extends regular Tenant object and includes Tenant Profile name. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the tenant name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, tenantProfileName, title, email, country, state, city, address, address2, zip, phone, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataTenantInfo**


## get_tenants

```python
PageDataTenant client.get_tenants(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenants`

Get Tenants (getTenants)

Returns a page of tenants registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the tenant name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, email, country, state, city, address, address2, zip, phone, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataTenant**


## get_tenants_by_ids

```python
List[Tenant] client.get_tenants_by_ids(tenant_ids: List[str])
```

**GET** `/api/tenants/list`

Get Tenants By Ids (getTenantsByIds)

Fetch Tenant objects based on the provided ids.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_ids** | **List[str]** | A list of tenant ids, separated by comma ',' | |

### Return type

**List[Tenant]**


## save_tenant

```python
Tenant client.save_tenant(tenant: Tenant)
```

**POST** `/api/tenant`

Create Or update Tenant (saveTenant)

Create or update the Tenant. When creating tenant, platform generates Tenant Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Default Rule Chain and Device profile are also generated for the new tenants automatically. The newly created Tenant Id will be present in the response. Specify existing Tenant Id id to update the Tenant. Referencing non-existing Tenant Id will cause 'Not Found' error.Remove 'id', 'tenantId' from the request body example (below) to create new Tenant entity.  Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant** | **Tenant** |  | |

### Return type

**Tenant**

