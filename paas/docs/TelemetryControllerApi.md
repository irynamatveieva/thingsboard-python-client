# TelemetryControllerApi

`ThingsboardClient` methods:

```python
str client.delete_device_attributes(device_id: str, scope: str, keys: Optional[str] = None, key: Optional[List[str]] = None)  # Delete device attributes (deleteDeviceAttributes)
str client.delete_entity_attributes(entity_type: str, entity_id: str, scope: str, keys: Optional[str] = None, key: Optional[List[str]] = None)  # Delete entity attributes (deleteEntityAttributes)
str client.delete_entity_timeseries(entity_type: str, entity_id: str, keys: Optional[str] = None, delete_all_data_for_keys: Optional[bool] = None, start_ts: Optional[int] = None, end_ts: Optional[int] = None, delete_latest: Optional[bool] = None, rewrite_latest_if_deleted: Optional[bool] = None, key: Optional[List[str]] = None)  # Delete entity time series data (deleteEntityTimeseries)
List[str] client.get_attribute_keys(entity_type: str, entity_id: str)  # Get all attribute keys (getAttributeKeys)
List[str] client.get_attribute_keys_by_scope(entity_type: str, entity_id: str, scope: str)  # Get all attribute keys by scope (getAttributeKeysByScope)
List[AttributeData] client.get_attributes(entity_type: str, entity_id: str, keys: Optional[str] = None, key: Optional[List[str]] = None)  # Get attributes (getAttributes)
List[AttributeData] client.get_attributes_by_scope(entity_type: str, entity_id: str, scope: str, keys: Optional[str] = None, key: Optional[List[str]] = None)  # Get attributes by scope (getAttributesByScope)
Dict[str, List[TsData]] client.get_latest_timeseries(entity_type: str, entity_id: str, keys: Optional[str] = None, use_strict_data_types: Optional[bool] = None, key: Optional[List[str]] = None)  # Get latest time series value (getLatestTimeseries)
List[ReadTsKvQueryResult] client.get_timeseries_by_read_ts_kv_queries(entity_type: str, entity_id: str, base_read_ts_kv_query: List[BaseReadTsKvQuery])  # Get time series data by read queries (getTimeseriesByReadTsKvQueries)
Dict[str, List[TsData]] client.get_timeseries_history(entity_type: str, entity_id: str, start_ts: int, end_ts: int, keys: Optional[str] = None, interval_type: Optional[str] = None, interval: Optional[int] = None, time_zone: Optional[str] = None, limit: Optional[str] = None, agg: Optional[str] = None, order_by: Optional[str] = None, use_strict_data_types: Optional[bool] = None, key: Optional[List[str]] = None)  # Get time series data (getTimeseriesHistory)
List[str] client.get_timeseries_keys(entity_type: str, entity_id: str)  # Get time series keys (getTimeseriesKeys)
str client.save_device_attributes(device_id: str, scope: str, body: str)  # Save device attributes (saveDeviceAttributes)
str client.save_entity_attributes_v1(entity_type: str, entity_id: str, scope: str, body: str)  # Save entity attributes (saveEntityAttributesV1)
str client.save_entity_attributes_v2(entity_type: str, entity_id: str, scope: str, body: str)  # Save entity attributes (saveEntityAttributesV2)
str client.save_entity_telemetry(entity_type: str, entity_id: str, scope: str, body: str)  # Save or update time series data (saveEntityTelemetry)
str client.save_entity_telemetry_with_ttl(entity_type: str, entity_id: str, scope: str, ttl: int, body: str)  # Save or update time series data with TTL (saveEntityTelemetryWithTTL)
```


## delete_device_attributes

```python
str client.delete_device_attributes(device_id: str, scope: str, keys: Optional[str] = None, key: Optional[List[str]] = None)
```

**DELETE** `/api/plugins/telemetry/{deviceId}/{scope}`

Delete device attributes (deleteDeviceAttributes)

Delete device attributes using provided Device Id, scope and a list of keys. Referencing a non-existing Device Id will cause an error  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | A string value representing the attributes scope. For example, 'SERVER_SCOPE'. | [enum: SERVER_SCOPE, SHARED_SCOPE, CLIENT_SCOPE] |
| **keys** | **str** | A string value representing the comma-separated list of attributes keys. For example, 'active,inactivityAlarmTime'. If attribute keys contain comma, duplicate 'key' parameter for each key, for example '?key=my,key&key=my,second,key | [optional] |
| **key** | **List[str]** | Repeatable key query parameter (alternative to comma-separated 'keys') | [optional] |

### Return type

**str**


## delete_entity_attributes

```python
str client.delete_entity_attributes(entity_type: str, entity_id: str, scope: str, keys: Optional[str] = None, key: Optional[List[str]] = None)
```

**DELETE** `/api/plugins/telemetry/{entityType}/{entityId}/{scope}`

Delete entity attributes (deleteEntityAttributes)

Delete entity attributes using provided Entity Id, scope and a list of keys. This operation is idempotent: keys that do not exist are silently ignored and the response is still 200 OK. Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | A string value representing the attributes scope. For example, 'SERVER_SCOPE'. | [enum: SERVER_SCOPE, SHARED_SCOPE, CLIENT_SCOPE] |
| **keys** | **str** | A string value representing the comma-separated list of attributes keys. For example, 'active,inactivityAlarmTime'. If attribute keys contain comma, duplicate 'key' parameter for each key, for example '?key=my,key&key=my,second,key | [optional] |
| **key** | **List[str]** | Repeatable key query parameter (alternative to comma-separated 'keys') | [optional] |

### Return type

**str**


## delete_entity_timeseries

```python
str client.delete_entity_timeseries(entity_type: str, entity_id: str, keys: Optional[str] = None, delete_all_data_for_keys: Optional[bool] = None, start_ts: Optional[int] = None, end_ts: Optional[int] = None, delete_latest: Optional[bool] = None, rewrite_latest_if_deleted: Optional[bool] = None, key: Optional[List[str]] = None)
```

**DELETE** `/api/plugins/telemetry/{entityType}/{entityId}/timeseries/delete`

Delete entity time series data (deleteEntityTimeseries)

Delete time series for selected entity based on entity id, entity type and keys. Use 'deleteAllDataForKeys' to delete all time series data. Use 'startTs' and 'endTs' to specify time-range instead.  Use 'deleteLatest' to delete latest value (stored in separate table for performance) if the value's timestamp matches the time-range.  Use 'rewriteLatestIfDeleted' to rewrite latest value (stored in separate table for performance) if the value's timestamp matches the time-range and 'deleteLatest' param is true. The replacement value will be fetched from the 'time series' table, and its timestamp will be the most recent one before the defined time-range.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **keys** | **str** | A string value representing the comma-separated list of telemetry keys. If keys are not selected, the result will return all latest time series. For example, 'temperature,humidity'. If telemetry keys contain comma, duplicate 'key' parameter for each key, for example '?key=my,key&key=my,second,key | [optional] |
| **delete_all_data_for_keys** | **bool** | A boolean value to specify if should be deleted all data for selected keys or only data that are in the selected time range. | [optional] [default to False] |
| **start_ts** | **int** | A long value representing the start timestamp of removal time range in milliseconds. | [optional] |
| **end_ts** | **int** | A long value representing the end timestamp of removal time range in milliseconds. | [optional] |
| **delete_latest** | **bool** | If the parameter is set to true, the latest telemetry can be removed, otherwise, in case that parameter is set to false the latest value will not removed. | [optional] [default to True] |
| **rewrite_latest_if_deleted** | **bool** | If the parameter is set to true, the latest telemetry will be rewritten in case that current latest value was removed, otherwise, in case that parameter is set to false the new latest value will not set. | [optional] [default to False] |
| **key** | **List[str]** | Repeatable key query parameter (alternative to comma-separated 'keys') | [optional] |

### Return type

**str**


## get_attribute_keys

```python
List[str] client.get_attribute_keys(entity_type: str, entity_id: str)
```

**GET** `/api/plugins/telemetry/{entityType}/{entityId}/keys/attributes`

Get all attribute keys (getAttributeKeys)

Returns a set of unique attribute key names for the selected entity. The response will include merged key names set for all attribute scopes:   * SERVER_SCOPE - supported for all entity types;  * CLIENT_SCOPE - supported for devices;  * SHARED_SCOPE - supported for devices.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[str]**


## get_attribute_keys_by_scope

```python
List[str] client.get_attribute_keys_by_scope(entity_type: str, entity_id: str, scope: str)
```

**GET** `/api/plugins/telemetry/{entityType}/{entityId}/keys/attributes/{scope}`

Get all attribute keys by scope (getAttributeKeysByScope)

Returns a set of unique attribute key names for the selected entity and attributes scope:    * SERVER_SCOPE - supported for all entity types;  * CLIENT_SCOPE - supported for devices;  * SHARED_SCOPE - supported for devices.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | A string value representing the attributes scope. For example, 'SERVER_SCOPE'. | [enum: SERVER_SCOPE, SHARED_SCOPE, CLIENT_SCOPE] |

### Return type

**List[str]**


## get_attributes

```python
List[AttributeData] client.get_attributes(entity_type: str, entity_id: str, keys: Optional[str] = None, key: Optional[List[str]] = None)
```

**GET** `/api/plugins/telemetry/{entityType}/{entityId}/values/attributes`

Get attributes (getAttributes)

Returns all attributes that belong to specified entity. Use optional 'keys' parameter to return specific attributes.  Example of the result:   ```json [   {\"key\": \"stringAttributeKey\", \"value\": \"value\", \"lastUpdateTs\": 1609459200000},   {\"key\": \"booleanAttributeKey\", \"value\": false, \"lastUpdateTs\": 1609459200001},   {\"key\": \"doubleAttributeKey\", \"value\": 42.2, \"lastUpdateTs\": 1609459200002},   {\"key\": \"longKeyExample\", \"value\": 73, \"lastUpdateTs\": 1609459200003},   {\"key\": \"jsonKeyExample\",     \"value\": {       \"someNumber\": 42,       \"someArray\": [1,2,3],       \"someNestedObject\": {\"key\": \"value\"}     },     \"lastUpdateTs\": 1609459200004   } ] ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **keys** | **str** | A string value representing the comma-separated list of attributes keys. For example, 'active,inactivityAlarmTime'. If attribute keys contain comma, duplicate 'key' parameter for each key, for example '?key=my,key&key=my,second,key | [optional] |
| **key** | **List[str]** | Repeatable key query parameter (alternative to comma-separated 'keys') | [optional] |

### Return type

**List[AttributeData]**


## get_attributes_by_scope

```python
List[AttributeData] client.get_attributes_by_scope(entity_type: str, entity_id: str, scope: str, keys: Optional[str] = None, key: Optional[List[str]] = None)
```

**GET** `/api/plugins/telemetry/{entityType}/{entityId}/values/attributes/{scope}`

Get attributes by scope (getAttributesByScope)

Returns all attributes of a specified scope that belong to specified entity. List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices;  * CLIENT_SCOPE - supported for devices.   Use optional 'keys' parameter to return specific attributes.  Example of the result:   ```json [   {\"key\": \"stringAttributeKey\", \"value\": \"value\", \"lastUpdateTs\": 1609459200000},   {\"key\": \"booleanAttributeKey\", \"value\": false, \"lastUpdateTs\": 1609459200001},   {\"key\": \"doubleAttributeKey\", \"value\": 42.2, \"lastUpdateTs\": 1609459200002},   {\"key\": \"longKeyExample\", \"value\": 73, \"lastUpdateTs\": 1609459200003},   {\"key\": \"jsonKeyExample\",     \"value\": {       \"someNumber\": 42,       \"someArray\": [1,2,3],       \"someNestedObject\": {\"key\": \"value\"}     },     \"lastUpdateTs\": 1609459200004   } ] ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | A string value representing the attributes scope. For example, 'SERVER_SCOPE'. | [enum: SERVER_SCOPE, SHARED_SCOPE, CLIENT_SCOPE] |
| **keys** | **str** | A string value representing the comma-separated list of attributes keys. For example, 'active,inactivityAlarmTime'. If attribute keys contain comma, duplicate 'key' parameter for each key, for example '?key=my,key&key=my,second,key | [optional] |
| **key** | **List[str]** | Repeatable key query parameter (alternative to comma-separated 'keys') | [optional] |

### Return type

**List[AttributeData]**


## get_latest_timeseries

```python
Dict[str, List[TsData]] client.get_latest_timeseries(entity_type: str, entity_id: str, keys: Optional[str] = None, use_strict_data_types: Optional[bool] = None, key: Optional[List[str]] = None)
```

**GET** `/api/plugins/telemetry/{entityType}/{entityId}/values/timeseries`

Get latest time series value (getLatestTimeseries)

Returns all time series that belong to specified entity. Use optional 'keys' parameter to return specific time series. The result is a JSON object. The format of the values depends on the 'useStrictDataTypes' parameter. By default, all time series values are converted to strings:   ```json {   \"stringTsKey\": [{ \"value\": \"value\", \"ts\": 1609459200000}],   \"booleanTsKey\": [{ \"value\": \"false\", \"ts\": 1609459200000}],   \"doubleTsKey\": [{ \"value\": \"42.2\", \"ts\": 1609459200000}],   \"longTsKey\": [{ \"value\": \"73\", \"ts\": 1609459200000}],   \"jsonTsKey\": [{ \"value\": \"{\\\"someNumber\\\": 42,\\\"someArray\\\": [1,2,3],\\\"someNestedObject\\\": {\\\"key\\\": \\\"value\\\"}}\", \"ts\": 1609459200000}] }  ```   However, it is possible to request the values without conversion ('useStrictDataTypes'=true):   ```json {   \"stringTsKey\": [{ \"value\": \"value\", \"ts\": 1609459200000}],   \"booleanTsKey\": [{ \"value\": false, \"ts\": 1609459200000}],   \"doubleTsKey\": [{ \"value\": 42.2, \"ts\": 1609459200000}],   \"longTsKey\": [{ \"value\": 73, \"ts\": 1609459200000}],   \"jsonTsKey\": [{      \"value\": {       \"someNumber\": 42,       \"someArray\": [1,2,3],       \"someNestedObject\": {\"key\": \"value\"}     },      \"ts\": 1609459200000}] }  ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **keys** | **str** | A string value representing the comma-separated list of telemetry keys. If keys are not selected, the result will return all latest time series. For example, 'temperature,humidity'. If telemetry keys contain comma, duplicate 'key' parameter for each key, for example '?key=my,key&key=my,second,key | [optional] |
| **use_strict_data_types** | **bool** | Enables/disables conversion of telemetry values to strings. Conversion is enabled by default. Set parameter to 'true' in order to disable the conversion. | [optional] [default to False] |
| **key** | **List[str]** | Repeatable key query parameter (alternative to comma-separated 'keys') | [optional] |

### Return type

**Dict[str, List[TsData]]**


## get_timeseries_by_read_ts_kv_queries

```python
List[ReadTsKvQueryResult] client.get_timeseries_by_read_ts_kv_queries(entity_type: str, entity_id: str, base_read_ts_kv_query: List[BaseReadTsKvQuery])
```

**POST** `/api/plugins/telemetry/{entityType}/{entityId}/values/timeseries`

Get time series data by read queries (getTimeseriesByReadTsKvQueries)

Returns aggregated time series values according to queries for specified entity. ```json [   {     \"queryId\": 49,     \"data\": [       {         \"ts\": 1751450399999,         \"kv\": {           \"key\": \"temperature\",           \"value\": 26,           \"doubleValue\": 26,           \"valueAsString\": \"26.0\",           \"dataType\": \"DOUBLE\",           \"longValue\": null,           \"booleanValue\": null,           \"jsonValue\": null,           \"strValue\": null         },         \"version\": null       }     ],     \"lastEntryTs\": 1750264592675   },   {     \"queryId\": 50,     \"data\": [],     \"lastEntryTs\": 1751317200000   } ] ```  Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **base_read_ts_kv_query** | **List[BaseReadTsKvQuery]** | A JSON array of time series read queries. | |

### Return type

**List[ReadTsKvQueryResult]**


## get_timeseries_history

```python
Dict[str, List[TsData]] client.get_timeseries_history(entity_type: str, entity_id: str, start_ts: int, end_ts: int, keys: Optional[str] = None, interval_type: Optional[str] = None, interval: Optional[int] = None, time_zone: Optional[str] = None, limit: Optional[str] = None, agg: Optional[str] = None, order_by: Optional[str] = None, use_strict_data_types: Optional[bool] = None, key: Optional[List[str]] = None)
```

**GET** `/api/plugins/telemetry/{entityType}/{entityId}/values/timeseries/history`

Get time series data (getTimeseriesHistory)

Returns a range of time series values for specified entity. Returns not aggregated data by default. Use aggregation function ('agg') and aggregation interval ('interval') to enable aggregation of the results on the database / server side. The aggregation is generally more efficient then fetching all records.   ```json {   \"temperature\": [     {       \"value\": 36.7,       \"ts\": 1609459200000     },     {       \"value\": 36.6,       \"ts\": 1609459201000     }   ] } ```  Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **start_ts** | **int** | A long value representing the start timestamp of the time range in milliseconds, UTC. | |
| **end_ts** | **int** | A long value representing the end timestamp of the time range in milliseconds, UTC. | |
| **keys** | **str** | A string value representing the comma-separated list of telemetry keys. | [optional] |
| **interval_type** | **str** | A string value representing the type fo the interval. | [optional] [enum: MILLISECONDS, WEEK, WEEK_ISO, MONTH, QUARTER] |
| **interval** | **int** | A long value representing the aggregation interval range in milliseconds. | [optional] [default to 0] |
| **time_zone** | **str** | A string value representing the timezone that will be used to calculate exact timestamps for 'WEEK', 'WEEK_ISO', 'MONTH' and 'QUARTER' interval types. | [optional] |
| **limit** | **str** | An integer value that represents a max number of time series data points to fetch. This parameter is used only in the case if 'agg' parameter is set to 'NONE'. | [optional] |
| **agg** | **str** | A string value representing the aggregation function. If the interval is not specified, 'agg' parameter will use 'NONE' value. | [optional] [enum: MIN, MAX, AVG, SUM, COUNT, NONE] |
| **order_by** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **use_strict_data_types** | **bool** | Enables/disables conversion of telemetry values to strings. Conversion is enabled by default. Set parameter to 'true' in order to disable the conversion. | [optional] [default to False] |
| **key** | **List[str]** | Repeatable key query parameter (alternative to comma-separated 'keys') | [optional] |

### Return type

**Dict[str, List[TsData]]**


## get_timeseries_keys

```python
List[str] client.get_timeseries_keys(entity_type: str, entity_id: str)
```

**GET** `/api/plugins/telemetry/{entityType}/{entityId}/keys/timeseries`

Get time series keys (getTimeseriesKeys)

Returns a set of unique time series key names for the selected entity.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[str]**


## save_device_attributes

```python
str client.save_device_attributes(device_id: str, scope: str, body: str)
```

**POST** `/api/plugins/telemetry/{deviceId}/{scope}`

Save device attributes (saveDeviceAttributes)

Creates or updates the device attributes based on device id and specified attribute scope. The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  \"stringKey\":\"value1\",   \"booleanKey\":true,   \"doubleKey\":42.0,   \"longKey\":73,   \"jsonKey\": {     \"someNumber\": 42,     \"someArray\": [1,2,3],     \"someNestedObject\": {\"key\": \"value\"}  } } ```   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | A string value representing the attributes scope. For example, 'SERVER_SCOPE'. | [enum: SERVER_SCOPE, SHARED_SCOPE] |
| **body** | **str** | A string value representing the json object. For example, '{\"key\":\"value\"}'. See API call description for more details. | |

### Return type

**str**


## save_entity_attributes_v1

```python
str client.save_entity_attributes_v1(entity_type: str, entity_id: str, scope: str, body: str)
```

**POST** `/api/plugins/telemetry/{entityType}/{entityId}/{scope}`

Save entity attributes (saveEntityAttributesV1)

Creates or updates the entity attributes based on Entity Id and the specified attribute scope.  List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices.  The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  \"stringKey\":\"value1\",   \"booleanKey\":true,   \"doubleKey\":42.0,   \"longKey\":73,   \"jsonKey\": {     \"someNumber\": 42,     \"someArray\": [1,2,3],     \"someNestedObject\": {\"key\": \"value\"}  } } ``` Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | A string value representing the attributes scope. For example, 'SERVER_SCOPE'. | [enum: SERVER_SCOPE, SHARED_SCOPE] |
| **body** | **str** | A string value representing the json object. For example, '{\"key\":\"value\"}'. See API call description for more details. | |

### Return type

**str**


## save_entity_attributes_v2

```python
str client.save_entity_attributes_v2(entity_type: str, entity_id: str, scope: str, body: str)
```

**POST** `/api/plugins/telemetry/{entityType}/{entityId}/attributes/{scope}`

Save entity attributes (saveEntityAttributesV2)

Creates or updates the entity attributes based on Entity Id and the specified attribute scope.  List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices.  The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  \"stringKey\":\"value1\",   \"booleanKey\":true,   \"doubleKey\":42.0,   \"longKey\":73,   \"jsonKey\": {     \"someNumber\": 42,     \"someArray\": [1,2,3],     \"someNestedObject\": {\"key\": \"value\"}  } } ``` Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | A string value representing the attributes scope. For example, 'SERVER_SCOPE'. | [enum: SERVER_SCOPE, SHARED_SCOPE] |
| **body** | **str** | A string value representing the json object. For example, '{\"key\":\"value\"}'. See API call description for more details. | |

### Return type

**str**


## save_entity_telemetry

```python
str client.save_entity_telemetry(entity_type: str, entity_id: str, scope: str, body: str)
```

**POST** `/api/plugins/telemetry/{entityType}/{entityId}/timeseries/{scope}`

Save or update time series data (saveEntityTelemetry)

Creates or updates the entity time series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:   ```json {\"temperature\": 26} ```   Single JSON object with timestamp:   ```json {\"ts\":1634712287000,\"values\":{\"temperature\":26, \"humidity\":87}} ```   JSON array with timestamps:   ```json [{\"ts\":1634712287000,\"values\":{\"temperature\":26, \"humidity\":87}}, {\"ts\":1634712588000,\"values\":{\"temperature\":25, \"humidity\":88}}] ```   The scope parameter is not used in the API call implementation but should be specified whatever value because it is used as a path variable. Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | Value is deprecated, reserved for backward compatibility and not used in the API call implementation. Specify any scope for compatibility | [enum: ANY] |
| **body** | **str** | A JSON with the telemetry values. See API call description for more details. | |

### Return type

**str**


## save_entity_telemetry_with_ttl

```python
str client.save_entity_telemetry_with_ttl(entity_type: str, entity_id: str, scope: str, ttl: int, body: str)
```

**POST** `/api/plugins/telemetry/{entityType}/{entityId}/timeseries/{scope}/{ttl}`

Save or update time series data with TTL (saveEntityTelemetryWithTTL)

Creates or updates the entity time series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:   ```json {\"temperature\": 26} ```   Single JSON object with timestamp:   ```json {\"ts\":1634712287000,\"values\":{\"temperature\":26, \"humidity\":87}} ```   JSON array with timestamps:   ```json [{\"ts\":1634712287000,\"values\":{\"temperature\":26, \"humidity\":87}}, {\"ts\":1634712588000,\"values\":{\"temperature\":25, \"humidity\":88}}] ```   The scope parameter is not used in the API call implementation but should be specified whatever value because it is used as a path variable.   The ttl parameter takes affect only in case of Cassandra DB.Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scope** | **str** | Value is deprecated, reserved for backward compatibility and not used in the API call implementation. Specify any scope for compatibility | [enum: ANY] |
| **ttl** | **int** | A long value representing TTL (Time to Live) parameter. | |
| **body** | **str** | A JSON with the telemetry values. See API call description for more details. | |

### Return type

**str**

