# TrendzControllerApi

`ThingsboardClient` methods:

```python
TrendzSynchronizationResult client.connect_to_trendz()  # Connect to Trendz (connectToTrendz)
TrendzConfiguration client.get_trendz_config()  # Get Trendz configuration (getTrendzConfig)
TrendzSynchronizationResult client.get_trendz_sync_result()  # Get Trendz synchronization result (getTrendzSyncResult)
TrendzHealthcheckResult client.perform_trendz_healthcheck()  # Perform Trendz healthcheck (performTrendzHealthcheck)
None client.public_connect_to_trendz()  # Public connect to Trendz (publicConnectToTrendz)
TrendzConfiguration client.save_trendz_config(trendz_configuration: TrendzConfiguration)  # Save Trendz configuration (saveTrendzConfig)
```


## connect_to_trendz

```python
TrendzSynchronizationResult client.connect_to_trendz()
```

**POST** `/api/trendz/connect`

Connect to Trendz (connectToTrendz)

Initiates synchronization with Trendz (Connect button action). Uses Trendz configuration from settings or falls back to environment variables. Generates API key, saves configuration, checks Trendz version, and performs initial sync.   Available for users with 'SYS_ADMIN' authority.

### Return type

**TrendzSynchronizationResult**


## get_trendz_config

```python
TrendzConfiguration client.get_trendz_config()
```

**GET** `/api/trendz/config`

Get Trendz configuration (getTrendzConfig)

Retrieves Trendz configuration (URLs). Returns trendzUrl and tbUrl.  Available for users with 'SYS_ADMIN' authority.

### Return type

**TrendzConfiguration**


## get_trendz_sync_result

```python
TrendzSynchronizationResult client.get_trendz_sync_result()
```

**GET** `/api/trendz/sync`

Get Trendz synchronization result (getTrendzSyncResult)

Retrieves Trendz synchronization result and status. Returns trendzVersion, updatedTs, resultType, and status.  Available for any authorized user. 

### Return type

**TrendzSynchronizationResult**


## perform_trendz_healthcheck

```python
TrendzHealthcheckResult client.perform_trendz_healthcheck()
```

**GET** `/api/trendz/healthcheck`

Perform Trendz healthcheck (performTrendzHealthcheck)

Performs healthcheck for Trendz integration. Returns version, type, status, and message. Can only be performed if Trendz is already synchronized and integration is enabled.  Available for any authorized user. 

### Return type

**TrendzHealthcheckResult**


## public_connect_to_trendz

```python
None client.public_connect_to_trendz()
```

**POST** `/api/trendz/public/connect`

Public connect to Trendz (publicConnectToTrendz)

Initiates synchronization with Trendz if Trendz is not synced yet. Uses Trendz configuration from settings or falls back to environment variables. Generates API key, saves configuration, checks Trendz version, and performs initial sync.

### Return type

None (empty response body)


## save_trendz_config

```python
TrendzConfiguration client.save_trendz_config(trendz_configuration: TrendzConfiguration)
```

**POST** `/api/trendz/config`

Save Trendz configuration (saveTrendzConfig)

Saves Trendz configuration (URLs only, without triggering synchronization). Request body example: ```json {   \"trendzUrl\": \"https://trendz.domain.com\",   \"tbUrl\": \"https://thingsboard.domain.com\" } ```  Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **trendz_configuration** | **TrendzConfiguration** |  | |

### Return type

**TrendzConfiguration**

