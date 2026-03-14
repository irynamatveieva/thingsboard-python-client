# TrendzControllerApi

`ThingsboardClient` methods:

```python
TrendzSettings client.get_trendz_settings()  # Get Trendz Settings (getTrendzSettings)
TrendzSettings client.save_trendz_settings(trendz_settings: TrendzSettings)  # Save Trendz settings (saveTrendzSettings)
```


## get_trendz_settings

```python
TrendzSettings client.get_trendz_settings()
```

**GET** `/api/trendz/settings`

Get Trendz Settings (getTrendzSettings)

Retrieves Trendz settings for this tenant.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**TrendzSettings**


## save_trendz_settings

```python
TrendzSettings client.save_trendz_settings(trendz_settings: TrendzSettings)
```

**POST** `/api/trendz/settings`

Save Trendz settings (saveTrendzSettings)

Saves Trendz settings for this tenant.   Here is an example of the Trendz settings: ```json {   \"enabled\": true,   \"baseUrl\": \"https://some.domain.com:18888/also_necessary_prefix\" } ```  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **trendz_settings** | **TrendzSettings** |  | |

### Return type

**TrendzSettings**

