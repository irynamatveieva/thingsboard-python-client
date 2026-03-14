# ImageControllerApi

`ThingsboardClient` methods:

```python
TbImageDeleteResult client.delete_image(type: str, key: str, force: Optional[bool] = None)  # deleteImage
bytearray client.download_image(type: str, key: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)  # downloadImage
bytearray client.download_image_preview(type: str, key: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)  # downloadImagePreview
bytearray client.download_public_image(public_resource_key: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)  # downloadPublicImage
ResourceExportData client.export_image(type: str, key: str)  # exportImage
TbResourceInfo client.get_image_info(type: str, key: str)  # getImageInfo
PageDataTbResourceInfo client.get_images(page_size: int, page: int, image_sub_type: Optional[str] = None, include_system_images: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # getImages
TbResourceInfo client.import_image(resource_export_data: ResourceExportData)  # importImage
TbResourceInfo client.update_image(type: str, key: str, file: bytearray)  # updateImage
TbResourceInfo client.update_image_info(type: str, key: str, tb_resource_info: TbResourceInfo)  # updateImageInfo
TbResourceInfo client.update_image_public_status(type: str, key: str, is_public: bool)  # updateImagePublicStatus
TbResourceInfo client.upload_image(file: bytearray, title: Optional[str] = None, image_sub_type: Optional[str] = None)  # uploadImage
```


## delete_image

```python
TbImageDeleteResult client.delete_image(type: str, key: str, force: Optional[bool] = None)
```

**DELETE** `/api/images/{type}/{key}`

deleteImage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |
| **force** | **bool** |  | [optional] |

### Return type

**TbImageDeleteResult**


## download_image

```python
bytearray client.download_image(type: str, key: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)
```

**GET** `/api/images/{type}/{key}`

downloadImage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |
| **if_none_match** | **str** |  | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**bytearray**


## download_image_preview

```python
bytearray client.download_image_preview(type: str, key: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)
```

**GET** `/api/images/{type}/{key}/preview`

downloadImagePreview


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |
| **if_none_match** | **str** |  | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**bytearray**


## download_public_image

```python
bytearray client.download_public_image(public_resource_key: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)
```

**GET** `/api/images/public/{publicResourceKey}`

downloadPublicImage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **public_resource_key** | **str** |  | |
| **if_none_match** | **str** |  | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**bytearray**


## export_image

```python
ResourceExportData client.export_image(type: str, key: str)
```

**GET** `/api/images/{type}/{key}/export`

exportImage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |

### Return type

**ResourceExportData**


## get_image_info

```python
TbResourceInfo client.get_image_info(type: str, key: str)
```

**GET** `/api/images/{type}/{key}/info`

getImageInfo


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |

### Return type

**TbResourceInfo**


## get_images

```python
PageDataTbResourceInfo client.get_images(page_size: int, page: int, image_sub_type: Optional[str] = None, include_system_images: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/images`

getImages


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **image_sub_type** | **str** | A string value representing resource sub-type. | [optional] [enum: IMAGE, SCADA_SYMBOL] |
| **include_system_images** | **bool** | Use 'true' to include system images. Disabled by default. Ignored for requests by users with system administrator authority. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the resource title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, resourceType, tenantId] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataTbResourceInfo**


## import_image

```python
TbResourceInfo client.import_image(resource_export_data: ResourceExportData)
```

**PUT** `/api/image/import`

importImage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_export_data** | **ResourceExportData** |  | |

### Return type

**TbResourceInfo**


## update_image

```python
TbResourceInfo client.update_image(type: str, key: str, file: bytearray)
```

**PUT** `/api/images/{type}/{key}`

updateImage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |
| **file** | **bytearray** |  | |

### Return type

**TbResourceInfo**


## update_image_info

```python
TbResourceInfo client.update_image_info(type: str, key: str, tb_resource_info: TbResourceInfo)
```

**PUT** `/api/images/{type}/{key}/info`

updateImageInfo


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |
| **tb_resource_info** | **TbResourceInfo** |  | |

### Return type

**TbResourceInfo**


## update_image_public_status

```python
TbResourceInfo client.update_image_public_status(type: str, key: str, is_public: bool)
```

**PUT** `/api/images/{type}/{key}/public/{isPublic}`

updateImagePublicStatus


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Type of the image: tenant or system | [enum: tenant, system] |
| **key** | **str** | Image resource key, for example thermostats_dashboard_background.jpeg | |
| **is_public** | **bool** |  | |

### Return type

**TbResourceInfo**


## upload_image

```python
TbResourceInfo client.upload_image(file: bytearray, title: Optional[str] = None, image_sub_type: Optional[str] = None)
```

**POST** `/api/image`

uploadImage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **file** | **bytearray** |  | |
| **title** | **str** |  | [optional] |
| **image_sub_type** | **str** |  | [optional] |

### Return type

**TbResourceInfo**

