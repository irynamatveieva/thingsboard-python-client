# CalculatedFieldControllerApi

`ThingsboardClient` methods:

```python
None client.delete_calculated_field(calculated_field_id: str)  # Delete Calculated Field (deleteCalculatedField)
CalculatedField client.get_calculated_field_by_id(calculated_field_id: str)  # Get Calculated Field (getCalculatedFieldById)
PageDataString client.get_calculated_field_names(type: CalculatedFieldType, page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None)  # Get calculated field names (getCalculatedFieldNames)
PageDataCalculatedFieldInfo client.get_calculated_fields(page_size: int, page: int, types: Optional[List[CalculatedFieldType]] = None, entity_type: Optional[EntityType] = None, entities: Optional[List[UUID]] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, name: Optional[List[str]] = None)  # Get calculated fields (getCalculatedFields)
PageDataCalculatedField client.get_calculated_fields_by_entity_id(entity_type: str, entity_id: str, page_size: int, page: int, type: Optional[CalculatedFieldType] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Calculated Fields by Entity Id (getCalculatedFieldsByEntityId)
object client.get_latest_calculated_field_debug_event(calculated_field_id: str)  # Get latest calculated field debug event (getLatestCalculatedFieldDebugEvent)
CalculatedField client.save_calculated_field(calculated_field: CalculatedField)  # Create Or Update Calculated Field (saveCalculatedField)
object client.test_calculated_field_script(body: object)  # Test Script expression
```


## delete_calculated_field

```python
None client.delete_calculated_field(calculated_field_id: str)
```

**DELETE** `/api/calculatedField/{calculatedFieldId}`

Delete Calculated Field (deleteCalculatedField)

Deletes the calculated field. Referencing non-existing Calculated Field Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **calculated_field_id** | **str** |  | |

### Return type

None (empty response body)


## get_calculated_field_by_id

```python
CalculatedField client.get_calculated_field_by_id(calculated_field_id: str)
```

**GET** `/api/calculatedField/{calculatedFieldId}`

Get Calculated Field (getCalculatedFieldById)

Fetch the Calculated Field object based on the provided Calculated Field Id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **calculated_field_id** | **str** |  | |

### Return type

**CalculatedField**


## get_calculated_field_names

```python
PageDataString client.get_calculated_field_names(type: CalculatedFieldType, page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/calculatedFields/names`

Get calculated field names (getCalculatedFieldNames)

Fetch the list of calculated field names for specified type.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **CalculatedFieldType** | Calculated field type filter. | [enum: SIMPLE, SCRIPT, GEOFENCING, ALARM, PROPAGATION, RELATED_ENTITIES_AGGREGATION, ENTITY_AGGREGATION] |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the calculated field name. | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataString**


## get_calculated_fields

```python
PageDataCalculatedFieldInfo client.get_calculated_fields(page_size: int, page: int, types: Optional[List[CalculatedFieldType]] = None, entity_type: Optional[EntityType] = None, entities: Optional[List[UUID]] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, name: Optional[List[str]] = None)
```

**GET** `/api/calculatedFields`

Get calculated fields (getCalculatedFields)

Fetch tenant calculated fields based on the filter.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **types** | **List[CalculatedFieldType]** | Calculated field types filter. | [optional] |
| **entity_type** | **EntityType** | Entity type filter. If not specified, calculated fields for all supported entity types will be returned. | [optional] [enum: TENANT, CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, ALARM, RULE_CHAIN, RULE_NODE, ENTITY_VIEW, WIDGETS_BUNDLE, WIDGET_TYPE, TENANT_PROFILE, DEVICE_PROFILE, ASSET_PROFILE, API_USAGE_STATE, TB_RESOURCE, OTA_PACKAGE, EDGE, RPC, QUEUE, NOTIFICATION_TARGET, NOTIFICATION_TEMPLATE, NOTIFICATION_REQUEST, NOTIFICATION, NOTIFICATION_RULE, QUEUE_STATS, OAUTH2_CLIENT, DOMAIN, MOBILE_APP, MOBILE_APP_BUNDLE, CALCULATED_FIELD, JOB, ADMIN_SETTINGS, AI_MODEL, API_KEY] |
| **entities** | **List[UUID]** | Entities filter. If not specified, calculated fields for entity type filter will be returned. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the calculated field name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **name** | **List[str]** | Repeatable name query parameter | [optional] |

### Return type

**PageDataCalculatedFieldInfo**


## get_calculated_fields_by_entity_id

```python
PageDataCalculatedField client.get_calculated_fields_by_entity_id(entity_type: str, entity_id: str, page_size: int, page: int, type: Optional[CalculatedFieldType] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/calculatedField/{entityType}/{entityId}`

Get Calculated Fields by Entity Id (getCalculatedFieldsByEntityId)

Fetch the Calculated Fields based on the provided Entity Id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **CalculatedFieldType** | Calculated field type. If not specified, all types will be returned. | [optional] [enum: SIMPLE, SCRIPT, GEOFENCING, ALARM, PROPAGATION, RELATED_ENTITIES_AGGREGATION, ENTITY_AGGREGATION] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the calculated field name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataCalculatedField**


## get_latest_calculated_field_debug_event

```python
object client.get_latest_calculated_field_debug_event(calculated_field_id: str)
```

**GET** `/api/calculatedField/{calculatedFieldId}/debug`

Get latest calculated field debug event (getLatestCalculatedFieldDebugEvent)

Gets latest calculated field debug event for specified calculated field id. Referencing non-existing calculated field id will cause an error.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **calculated_field_id** | **str** |  | |

### Return type

**object**


## save_calculated_field

```python
CalculatedField client.save_calculated_field(calculated_field: CalculatedField)
```

**POST** `/api/calculatedField`

Create Or Update Calculated Field (saveCalculatedField)

Creates or Updates the Calculated Field. When creating calculated field, platform generates Calculated Field Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Calculated Field Id will be present in the response. Specify existing Calculated Field Id to update the calculated field. Referencing non-existing Calculated Field Id will cause 'Not Found' error. Remove 'id', 'tenantId' from the request body example (below) to create new Calculated Field entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **calculated_field** | **CalculatedField** | A JSON value representing the calculated field. | |

### Return type

**CalculatedField**


## test_calculated_field_script

```python
object client.test_calculated_field_script(body: object)
```

**POST** `/api/calculatedField/testScript`

Test Script expression

Execute the Script expression and return the result. The format of request:   ```json {   \"expression\": \"var temp = 0; foreach(element: temperature.values) {temp += element.value;} var avgTemperature = temp / temperature.values.size(); var adjustedTemperature = avgTemperature + 0.1 * humidity.value; return {\\\"adjustedTemperature\\\": adjustedTemperature};\",   \"arguments\": {     \"temperature\": {       \"type\": \"TS_ROLLING\",       \"timeWindow\": {         \"startTs\": 1739775630002,         \"endTs\": 65432211,         \"limit\": 5       },       \"values\": [         { \"ts\": 1739775639851, \"value\": 23 },         { \"ts\": 1739775664561, \"value\": 43 },         { \"ts\": 1739775713079, \"value\": 15 },         { \"ts\": 1739775999522, \"value\": 34 },         { \"ts\": 1739776228452, \"value\": 22 }       ]     },     \"humidity\": { \"type\": \"SINGLE_VALUE\", \"ts\": 1739776478057, \"value\": 23 }   } } ```   Expected result JSON contains \"output\" and \"error\".  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** | Test calculated field TBEL expression. | |

### Return type

**object**

