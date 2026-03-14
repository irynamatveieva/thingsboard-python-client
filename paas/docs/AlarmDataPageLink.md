
# AlarmDataPageLink

`tb_paas_client.models.AlarmDataPageLink`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **start_ts** | **int** |  | [optional] |
| **end_ts** | **int** |  | [optional] |
| **time_window** | **int** |  | [optional] |
| **type_list** | **List[str]** |  | [optional] |
| **status_list** | [**List[AlarmSearchStatus]**](AlarmSearchStatus.md) |  | [optional] |
| **severity_list** | [**List[AlarmSeverity]**](AlarmSeverity.md) |  | [optional] |
| **search_propagated_alarms** | **bool** |  | [optional] |
| **assignee_id** | [**UserId**](UserId.md) |  | [optional] |
| **page_size** | **int** |  | [optional] |
| **page** | **int** |  | [optional] |
| **text_search** | **str** |  | [optional] |
| **sort_order** | [**EntityDataSortOrder**](EntityDataSortOrder.md) |  | [optional] |
| **dynamic** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.start_ts`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmDataPageLink.model_validate(data)` or `AlarmDataPageLink.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

