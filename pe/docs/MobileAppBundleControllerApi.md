# MobileAppBundleControllerApi

`ThingsboardClient` methods:

```python
None client.delete_mobile_app_bundle(id: UUID)  # Delete Mobile App Bundle by ID (deleteMobileAppBundle)
MobileAppBundleInfo client.get_mobile_app_bundle_info_by_id(id: UUID)  # Get mobile app bundle info by id (getMobileAppBundleInfoById)
PageDataMobileAppBundleInfo client.get_tenant_mobile_app_bundle_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get mobile app bundle infos (getTenantMobileAppBundleInfos)
MobileAppBundle client.save_mobile_app_bundle(mobile_app_bundle: MobileAppBundle, oauth2_client_ids: Optional[List[str]] = None)  # Save Or update Mobile app bundle (saveMobileAppBundle)
None client.update_mobile_app_bundle_oauth2_clients(id: UUID, request_body: List[UUID])  # Update oauth2 clients (updateMobileAppBundleOauth2Clients)
```


## delete_mobile_app_bundle

```python
None client.delete_mobile_app_bundle(id: UUID)
```

**DELETE** `/api/mobile/bundle/{id}`

Delete Mobile App Bundle by ID (deleteMobileAppBundle)

Deletes Mobile App Bundle by ID. Referencing non-existing mobile app bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_mobile_app_bundle_info_by_id

```python
MobileAppBundleInfo client.get_mobile_app_bundle_info_by_id(id: UUID)
```

**GET** `/api/mobile/bundle/info/{id}`

Get mobile app bundle info by id (getMobileAppBundleInfoById)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**MobileAppBundleInfo**


## get_tenant_mobile_app_bundle_infos

```python
PageDataMobileAppBundleInfo client.get_tenant_mobile_app_bundle_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/mobile/bundle/infos`

Get mobile app bundle infos (getTenantMobileAppBundleInfos)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on app's name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataMobileAppBundleInfo**


## save_mobile_app_bundle

```python
MobileAppBundle client.save_mobile_app_bundle(mobile_app_bundle: MobileAppBundle, oauth2_client_ids: Optional[List[str]] = None)
```

**POST** `/api/mobile/bundle`

Save Or update Mobile app bundle (saveMobileAppBundle)

Create or update the Mobile app bundle that represents tha pair of ANDROID and IOS app and mobile settings like oauth2 clients, self-registration and layout configuration.When creating mobile app bundle, platform generates Mobile App Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Bundle Id will be present in the response. Referencing non-existing Mobile App Bundle Id will cause 'Not Found' error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mobile_app_bundle** | **MobileAppBundle** |  | |
| **oauth2_client_ids** | **List[str]** | A list of oauth2 client ids, separated by comma ',' | [optional] |

### Return type

**MobileAppBundle**


## update_mobile_app_bundle_oauth2_clients

```python
None client.update_mobile_app_bundle_oauth2_clients(id: UUID, request_body: List[UUID])
```

**PUT** `/api/mobile/bundle/{id}/oauth2Clients`

Update oauth2 clients (updateMobileAppBundleOauth2Clients)

Update oauth2 clients of the specified mobile app bundle.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |
| **request_body** | **List[UUID]** |  | |

### Return type

None (empty response body)

