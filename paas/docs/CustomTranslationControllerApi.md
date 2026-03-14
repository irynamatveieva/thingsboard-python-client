# CustomTranslationControllerApi

`ThingsboardClient` methods:

```python
None client.delete_custom_translation(locale_code: str)  # Delete Custom Translation for specified locale (deleteCustomTranslation)
None client.delete_custom_translation_key(locale_code: str, key_path: str)  # Delete specified key of Custom Translation (deleteCustomTranslationKey) 
object client.get_custom_translation(locale_code: str)  # Get Custom Translation configuration (getCustomTranslation)
object client.get_merged_custom_translation(locale_code: str)  # Get end-user Custom Translation configuration (getMergedCustomTranslation)
None client.patch_custom_translation(locale_code: str, body: object)  # Update Custom Translation for specified translation keys only (patchCustomTranslation)
None client.save_custom_translation(locale_code: str, body: object)  # Create Or Update Custom Translation (saveCustomTranslation)
None client.upload_custom_translation(locale_code: str, file: bytearray)  # Upload Custom Translation (uploadCustomTranslation)
```


## delete_custom_translation

```python
None client.delete_custom_translation(locale_code: str)
```

**DELETE** `/api/translation/custom/{localeCode}`

Delete Custom Translation for specified locale (deleteCustomTranslation)

Delete entire custom translation settings for end-user  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |

### Return type

None (empty response body)


## delete_custom_translation_key

```python
None client.delete_custom_translation_key(locale_code: str, key_path: str)
```

**DELETE** `/api/translation/custom/{localeCode}/{keyPath}`

Delete specified key of Custom Translation (deleteCustomTranslationKey) 

The API call is designed to delete specified key of the custom translation and return as a result parent translation.(e.g. if tenant translation for key is 'value1' and customer translation is 'value2' then by deletinf key onn customer level you will get 'value1' in response)   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |
| **key_path** | **str** | A string value representing key of the custom translation (e.g. 'notification.active'). | |

### Return type

None (empty response body)


## get_custom_translation

```python
object client.get_custom_translation(locale_code: str)
```

**GET** `/api/translation/custom/{localeCode}`

Get Custom Translation configuration (getCustomTranslation)

Fetch the Custom Translation for specified locale that corresponds to the authority of the user. The API call is designed to load the custom translation items for edition. So, the result is NOT merged with the parent level configuration. Let's assume there is a custom translation configured on a system level. And there is no custom translation items configured on a tenant level. In such a case, the API call will return empty object for the tenant administrator.    Response example:   ```json {\"home\":\"MyHome\"} ```  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |

### Return type

**object**


## get_merged_custom_translation

```python
object client.get_merged_custom_translation(locale_code: str)
```

**GET** `/api/translation/custom/merged/{localeCode}`

Get end-user Custom Translation configuration (getMergedCustomTranslation)

Fetch end-user Custom Translation for specified locale. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |

### Return type

**object**


## patch_custom_translation

```python
None client.patch_custom_translation(locale_code: str, body: object)
```

**PATCH** `/api/translation/custom/{localeCode}`

Update Custom Translation for specified translation keys only (patchCustomTranslation)

The API call is designed to update the custom translation for specified key only.    Request example:   ```json {\"notification.active\":\"active\"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |
| **body** | **object** |  | |

### Return type

None (empty response body)


## save_custom_translation

```python
None client.save_custom_translation(locale_code: str, body: object)
```

**POST** `/api/translation/custom/{localeCode}`

Create Or Update Custom Translation (saveCustomTranslation)

Creates or Updates the Custom Translation for specified locale.   Request example:   ```json {\"home\":\"MyHome\"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |
| **body** | **object** |  | |

### Return type

None (empty response body)


## upload_custom_translation

```python
None client.upload_custom_translation(locale_code: str, file: bytearray)
```

**POST** `/api/translation/custom/{localeCode}/upload`

Upload Custom Translation (uploadCustomTranslation)

Upload the Custom Translation for specified locale.   Request example:   ```json {\"home\":\"MyHome\"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |
| **file** | **bytearray** |  | |

### Return type

None (empty response body)

