# MobileAppControllerApi

`ThingsboardClient` methods:

```python
None client.delete_mobile_app(id: UUID)  # Delete Mobile App by ID (deleteMobileApp)
LoginMobileInfo client.get_login_mobile_info(pkg_name: str, platform: str)  # Get mobile app login info (getLoginMobileInfo)
MobileApp client.get_mobile_app_by_id(id: UUID)  # Get mobile info by id (getMobileAppById)
PageDataMobileApp client.get_tenant_mobile_apps(page_size: int, page: int, platform_type: Optional[PlatformType] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get mobile app infos (getTenantMobileApps)
UserMobileInfo client.get_user_mobile_info(pkg_name: str, platform: str)  # Get user mobile app basic info (getUserMobileInfo)
MobileApp client.save_mobile_app(mobile_app: MobileApp)  # Save Or update Mobile app (saveMobileApp)
```


## delete_mobile_app

```python
None client.delete_mobile_app(id: UUID)
```

**DELETE** `/api/mobile/app/{id}`

Delete Mobile App by ID (deleteMobileApp)

Deletes Mobile App by ID. Referencing non-existing mobile app Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_login_mobile_info

```python
LoginMobileInfo client.get_login_mobile_info(pkg_name: str, platform: str)
```

**GET** `/api/noauth/mobile`

Get mobile app login info (getLoginMobileInfo)


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** | Mobile application package name | |
| **platform** | **str** | Platform type | [enum: ANDROID, IOS] |

### Return type

**LoginMobileInfo**


## get_mobile_app_by_id

```python
MobileApp client.get_mobile_app_by_id(id: UUID)
```

**GET** `/api/mobile/app/{id}`

Get mobile info by id (getMobileAppById)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**MobileApp**


## get_tenant_mobile_apps

```python
PageDataMobileApp client.get_tenant_mobile_apps(page_size: int, page: int, platform_type: Optional[PlatformType] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/mobile/app`

Get mobile app infos (getTenantMobileApps)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **platform_type** | **PlatformType** | Platform type: ANDROID or IOS | [optional] [enum: WEB, ANDROID, IOS] |
| **text_search** | **str** | Case-insensitive 'substring' filter based on app's name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataMobileApp**


## get_user_mobile_info

```python
UserMobileInfo client.get_user_mobile_info(pkg_name: str, platform: str)
```

**GET** `/api/mobile`

Get user mobile app basic info (getUserMobileInfo)

  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** | Mobile application package name | |
| **platform** | **str** | Platform type | [enum: ANDROID, IOS] |

### Return type

**UserMobileInfo**


## save_mobile_app

```python
MobileApp client.save_mobile_app(mobile_app: MobileApp)
```

**POST** `/api/mobile/app`

Save Or update Mobile app (saveMobileApp)

Create or update the Mobile app. When creating mobile app, platform generates Mobile App Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Id will be present in the response. Specify existing Mobile App Id to update the mobile app. Referencing non-existing Mobile App Id will cause 'Not Found' error.  The pair of mobile app package name and platform type is unique for entire platform setup.    Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mobile_app** | **MobileApp** |  | |

### Return type

**MobileApp**

