# AiModelControllerApi

`ThingsboardClient` methods:

```python
bool client.delete_ai_model_by_id(model_uuid: UUID)  # Delete AI model by ID (deleteAiModelById)
AiModel client.get_ai_model_by_id(model_uuid: UUID)  # Get AI model by ID (getAiModelById)
PageDataAiModel client.get_ai_models(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get AI models (getAiModels)
AiModel client.save_ai_model(ai_model: AiModel)  # Create or update AI model (saveAiModel)
TbChatResponse client.send_chat_request(tb_chat_request: TbChatRequest)  # Send request to AI chat model (sendChatRequest)
```


## delete_ai_model_by_id

```python
bool client.delete_ai_model_by_id(model_uuid: UUID)
```

**DELETE** `/api/ai/model/{modelUuid}`

Delete AI model by ID (deleteAiModelById)

Deletes the AI model record by its `id`. If a record with the specified `id` exists, the record is deleted and the endpoint returns `true`. If no such record exists, the endpoint returns `false`.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **model_uuid** | **UUID** | ID of the AI model record | |

### Return type

**bool**


## get_ai_model_by_id

```python
AiModel client.get_ai_model_by_id(model_uuid: UUID)
```

**GET** `/api/ai/model/{modelUuid}`

Get AI model by ID (getAiModelById)

Fetches an AI model record by its `id`.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **model_uuid** | **UUID** | ID of the AI model record | |

### Return type

**AiModel**


## get_ai_models

```python
PageDataAiModel client.get_ai_models(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/ai/model`

Get AI models (getAiModels)

Returns a page of AI models. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the AI model name, provider and model ID. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, provider, modelId] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAiModel**


## save_ai_model

```python
AiModel client.save_ai_model(ai_model: AiModel)
```

**POST** `/api/ai/model`

Create or update AI model (saveAiModel)

Creates or updates an AI model record.  • **Create:** Omit the `id` to create a new record. The platform assigns a UUID to the new record and returns it in the `id` field of the response.  • **Update:** Include an existing `id` to modify that record. If no matching record exists, the API responds with **404 Not Found**.  Tenant ID for the AI model will be taken from the authenticated user making the request, regardless of any value provided in the request body.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ai_model** | **AiModel** |  | |

### Return type

**AiModel**


## send_chat_request

```python
TbChatResponse client.send_chat_request(tb_chat_request: TbChatRequest)
```

**POST** `/api/ai/model/chat`

Send request to AI chat model (sendChatRequest)

Submits a single prompt - made up of an optional system message and a required user message - to the specified AI chat model and returns either the generated answer or an error envelope.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tb_chat_request** | **TbChatRequest** |  | |

### Return type

**TbChatResponse**

