# BlobEntityControllerApi

`ThingsboardClient` methods:

```python
None client.delete_blob_entity(blob_entity_id: str)  # Delete Blob Entity (deleteBlobEntity)
bytearray client.download_blob_entity(blob_entity_id: str)  # Download Blob Entity By Id (downloadBlobEntity)
PageDataBlobEntityWithCustomerInfo client.get_blob_entities(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)  # Get Blob Entities (getBlobEntities)
List[BlobEntityInfo] client.get_blob_entities_by_ids(blob_entity_ids: List[str])  # Get Blob Entities By Ids (getBlobEntitiesByIds)
BlobEntityWithCustomerInfo client.get_blob_entity_info_by_id(blob_entity_id: str)  # Get Blob Entity With Customer Info (getBlobEntityInfoById)
```


## delete_blob_entity

```python
None client.delete_blob_entity(blob_entity_id: str)
```

**DELETE** `/api/blobEntity/{blobEntityId}`

Delete Blob Entity (deleteBlobEntity)

Delete Blob entity based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **blob_entity_id** | **str** | A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## download_blob_entity

```python
bytearray client.download_blob_entity(blob_entity_id: str)
```

**GET** `/api/blobEntity/{blobEntityId}/download`

Download Blob Entity By Id (downloadBlobEntity)

Download report file based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **blob_entity_id** | **str** | A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**bytearray**


## get_blob_entities

```python
PageDataBlobEntityWithCustomerInfo client.get_blob_entities(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)
```

**GET** `/api/blobEntities`

Get Blob Entities (getBlobEntities)

Returns a page of BlobEntityWithCustomerInfo object that are available for the current user. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | A string value representing the blob entity type. For example, 'report' | [optional] |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the blob entity name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, contentType, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'. | [optional] |

### Return type

**PageDataBlobEntityWithCustomerInfo**


## get_blob_entities_by_ids

```python
List[BlobEntityInfo] client.get_blob_entities_by_ids(blob_entity_ids: List[str])
```

**GET** `/api/blobEntities/list`

Get Blob Entities By Ids (getBlobEntitiesByIds)

Requested blob entities must be owned by tenant or assigned to customer which user is performing the request. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.). See the 'Model' tab of the Response Class for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **blob_entity_ids** | **List[str]** | A list of blob entity ids, separated by comma ',' | |

### Return type

**List[BlobEntityInfo]**


## get_blob_entity_info_by_id

```python
BlobEntityWithCustomerInfo client.get_blob_entity_info_by_id(blob_entity_id: str)
```

**GET** `/api/blobEntity/info/{blobEntityId}`

Get Blob Entity With Customer Info (getBlobEntityInfoById)

Fetch the BlobEntityWithCustomerInfo object based on the provided Blob entity Id. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **blob_entity_id** | **str** | A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**BlobEntityWithCustomerInfo**

