# ApiKeyControllerApi

`ThingsboardClient` methods:

```python
None client.delete_api_key(id: UUID)  # Delete API key by ID (deleteApiKey)
ApiKeyInfo client.enable_api_key(id: UUID, enabled_value: bool)  # Enable or disable API key (enableApiKey)
PageDataApiKeyInfo client.get_user_api_keys(user_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get User Api Keys (getUserApiKeys)
ApiKey client.save_api_key(api_key_info: ApiKeyInfo)  # Save API key for user (saveApiKey)
ApiKeyInfo client.update_api_key_description(id: UUID, body: Optional[str] = None)  # Update API key Description
```


## delete_api_key

```python
None client.delete_api_key(id: UUID)
```

**DELETE** `/api/apiKey/{id}`

Delete API key by ID (deleteApiKey)

Deletes the API key. Referencing non-existing ApiKey Id will cause an error.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## enable_api_key

```python
ApiKeyInfo client.enable_api_key(id: UUID, enabled_value: bool)
```

**PUT** `/api/apiKey/{id}/enabled/{enabledValue}`

Enable or disable API key (enableApiKey)

Updates api key with enabled = true/false.   Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** | Unique identifier of the API key to enable/disable | |
| **enabled_value** | **bool** | Enabled or disabled api key | |

### Return type

**ApiKeyInfo**


## get_user_api_keys

```python
PageDataApiKeyInfo client.get_user_api_keys(user_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/apiKeys/{userId}`

Get User Api Keys (getUserApiKeys)

Returns a page of api keys owned by user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the description. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, expirationTime, description, enabled] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataApiKeyInfo**


## save_api_key

```python
ApiKey client.save_api_key(api_key_info: ApiKeyInfo)
```

**POST** `/api/apiKey`

Save API key for user (saveApiKey)

Creates an API key for the given user and returns the token ONCE as 'ApiKey {value}'.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **api_key_info** | **ApiKeyInfo** |  | |

### Return type

**ApiKey**


## update_api_key_description

```python
ApiKeyInfo client.update_api_key_description(id: UUID, body: Optional[str] = None)
```

**PUT** `/api/apiKey/{id}/description`

Update API key Description

Updates the description of the existing API key by apiKeyId. Only the description can be updated. Referencing a non-existing ApiKey Id will cause a 'Not Found' error.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** | A string value representing the api key id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **str** |  | [optional] |

### Return type

**ApiKeyInfo**

