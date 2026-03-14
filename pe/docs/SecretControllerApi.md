# SecretControllerApi

`ThingsboardClient` methods:

```python
TbSecretDeleteResult client.delete_secret(id: UUID)  # Delete secret by ID (deleteSecret)
SecretInfo client.get_secret_info_by_id(id: UUID)  # Get Secret info by Id (getSecretInfoById)
SecretInfo client.get_secret_info_by_name(name: str)  # Get Secret info by name (getSecretInfoByName)
PageDataSecretInfo client.get_secret_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Secret infos (getSecretInfos)
List[str] client.get_secret_names()  # Get Tenant Secret names (getSecretNames)
SecretInfo client.save_secret(secret: Secret)  # Save or Update Secret (saveSecret)
SecretInfo client.update_secret_description(id: UUID, body: Optional[str] = None)  # Update Secret Description
SecretInfo client.update_secret_value(id: UUID, body: str)  # Update Secret value
```


## delete_secret

```python
TbSecretDeleteResult client.delete_secret(id: UUID)
```

**DELETE** `/api/secret/{id}`

Delete secret by ID (deleteSecret)

Deletes the secret. Referencing non-existing Secret Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**TbSecretDeleteResult**


## get_secret_info_by_id

```python
SecretInfo client.get_secret_info_by_id(id: UUID)
```

**GET** `/api/secret/{id}/info`

Get Secret info by Id (getSecretInfoById)

  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**SecretInfo**


## get_secret_info_by_name

```python
SecretInfo client.get_secret_info_by_name(name: str)
```

**GET** `/api/secret`

Get Secret info by name (getSecretInfoByName)

  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **str** |  | |

### Return type

**SecretInfo**


## get_secret_infos

```python
PageDataSecretInfo client.get_secret_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/secrets`

Get Tenant Secret infos (getSecretInfos)

Returns a page of secret infos owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the secret name and description. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataSecretInfo**


## get_secret_names

```python
List[str] client.get_secret_names()
```

**GET** `/api/secret/names`

Get Tenant Secret names (getSecretNames)

Returns a page of secret names owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.

### Return type

**List[str]**


## save_secret

```python
SecretInfo client.save_secret(secret: Secret)
```

**POST** `/api/secret`

Save or Update Secret (saveSecret)

Create or update the Secret. When creating secret, platform generates Secret Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Secret Id will be present in the response. Specify existing Secret Id to update the secret. Secret name is not updatable, only value could be changed. Referencing non-existing Secret Id will cause 'Not Found' error.  Secret name is unique in the scope of tenant.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **secret** | **Secret** |  | |

### Return type

**SecretInfo**


## update_secret_description

```python
SecretInfo client.update_secret_description(id: UUID, body: Optional[str] = None)
```

**PUT** `/api/secret/{id}/description`

Update Secret Description

Updates the description of the existing Secret by secretId. Only the description can be updated. Referencing a non-existing Secret Id will cause a 'Not Found' error.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** | Unique identifier of the Secret to update | |
| **body** | **str** |  | [optional] |

### Return type

**SecretInfo**


## update_secret_value

```python
SecretInfo client.update_secret_value(id: UUID, body: str)
```

**PUT** `/api/secret/{id}/value`

Update Secret value

Updates the value of the existing Secret by secretId. Referencing a non-existing Secret Id will cause a 'Not Found' error.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** | Unique identifier of the Secret to update | |
| **body** | **str** |  | |

### Return type

**SecretInfo**

