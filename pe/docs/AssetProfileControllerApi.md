# AssetProfileControllerApi

`ThingsboardClient` methods:

```python
None client.delete_asset_profile(asset_profile_id: str)  # Delete asset profile (deleteAssetProfile)
AssetProfile client.get_asset_profile_by_id(asset_profile_id: str, inline_images: Optional[bool] = None)  # Get Asset Profile (getAssetProfileById)
AssetProfileInfo client.get_asset_profile_info_by_id(asset_profile_id: str)  # Get Asset Profile Info (getAssetProfileInfoById)
PageDataAssetProfileInfo client.get_asset_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Asset Profile infos (getAssetProfileInfos)
List[EntityInfo] client.get_asset_profile_names(active_only: Optional[bool] = None)  # Get Asset Profile names (getAssetProfileNames)
PageDataAssetProfile client.get_asset_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Asset Profiles (getAssetProfiles)
List[AssetProfileInfo] client.get_asset_profiles_by_ids(asset_profile_ids: List[str])  # Get Asset Profiles By Ids (getAssetProfilesByIds)
AssetProfileInfo client.get_default_asset_profile_info()  # Get Default Asset Profile (getDefaultAssetProfileInfo)
AssetProfile client.save_asset_profile(asset_profile: AssetProfile)  # Create Or Update Asset Profile (saveAssetProfile)
AssetProfile client.set_default_asset_profile(asset_profile_id: str)  # Make Asset Profile Default (setDefaultAssetProfile)
```


## delete_asset_profile

```python
None client.delete_asset_profile(asset_profile_id: str)
```

**DELETE** `/api/assetProfile/{assetProfileId}`

Delete asset profile (deleteAssetProfile)

Deletes the asset profile. Referencing non-existing asset profile Id will cause an error. Can't delete the asset profile if it is referenced by existing assets.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_asset_profile_by_id

```python
AssetProfile client.get_asset_profile_by_id(asset_profile_id: str, inline_images: Optional[bool] = None)
```

**GET** `/api/assetProfile/{assetProfileId}`

Get Asset Profile (getAssetProfileById)

Fetch the Asset Profile object based on the provided Asset Profile Id. The server checks that the asset profile is owned by the same tenant.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **inline_images** | **bool** | Inline images as a data URL (Base64) | [optional] |

### Return type

**AssetProfile**


## get_asset_profile_info_by_id

```python
AssetProfileInfo client.get_asset_profile_info_by_id(asset_profile_id: str)
```

**GET** `/api/assetProfileInfo/{assetProfileId}`

Get Asset Profile Info (getAssetProfileInfoById)

Fetch the Asset Profile Info object based on the provided Asset Profile Id. Asset Profile Info is a lightweight object that includes main information about Asset Profile.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AssetProfileInfo**


## get_asset_profile_infos

```python
PageDataAssetProfileInfo client.get_asset_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/assetProfileInfos`

Get Asset Profile infos (getAssetProfileInfos)

Returns a page of asset profile info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. Asset Profile Info is a lightweight object that includes main information about Asset Profile.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset profile name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, description, isDefault] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAssetProfileInfo**


## get_asset_profile_names

```python
List[EntityInfo] client.get_asset_profile_names(active_only: Optional[bool] = None)
```

**GET** `/api/assetProfile/names`

Get Asset Profile names (getAssetProfileNames)

Returns a set of unique asset profile names owned by the tenant.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **active_only** | **bool** | Flag indicating whether to retrieve exclusively the names of asset profiles that are referenced by tenant's assets. | [optional] [default to False] |

### Return type

**List[EntityInfo]**


## get_asset_profiles

```python
PageDataAssetProfile client.get_asset_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/assetProfiles`

Get Asset Profiles (getAssetProfiles)

Returns a page of asset profile objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset profile name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, description, isDefault] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAssetProfile**


## get_asset_profiles_by_ids

```python
List[AssetProfileInfo] client.get_asset_profiles_by_ids(asset_profile_ids: List[str])
```

**GET** `/api/assetProfileInfos/list`

Get Asset Profiles By Ids (getAssetProfilesByIds)

Requested asset profiles must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_profile_ids** | **List[str]** | A list of asset profile ids, separated by comma ',' | |

### Return type

**List[AssetProfileInfo]**


## get_default_asset_profile_info

```python
AssetProfileInfo client.get_default_asset_profile_info()
```

**GET** `/api/assetProfileInfo/default`

Get Default Asset Profile (getDefaultAssetProfileInfo)

Fetch the Default Asset Profile Info object. Asset Profile Info is a lightweight object that includes main information about Asset Profile.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**AssetProfileInfo**


## save_asset_profile

```python
AssetProfile client.save_asset_profile(asset_profile: AssetProfile)
```

**POST** `/api/assetProfile`

Create Or Update Asset Profile (saveAssetProfile)

Create or update the Asset Profile. When creating asset profile, platform generates asset profile id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created asset profile id will be present in the response. Specify existing asset profile id to update the asset profile. Referencing non-existing asset profile Id will cause 'Not Found' error.   Asset profile name is unique in the scope of tenant. Only one 'default' asset profile may exist in scope of tenant. Remove 'id', 'tenantId' from the request body example (below) to create new Asset Profile entity.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_profile** | **AssetProfile** |  | |

### Return type

**AssetProfile**


## set_default_asset_profile

```python
AssetProfile client.set_default_asset_profile(asset_profile_id: str)
```

**POST** `/api/assetProfile/{assetProfileId}/default`

Make Asset Profile Default (setDefaultAssetProfile)

Marks asset profile as default within a tenant scope.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AssetProfile**

