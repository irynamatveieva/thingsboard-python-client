
# AlarmFilterConfig

`tb_paas_client.models.AlarmFilterConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type_list** | **List[str]** |  | [optional] |
| **status_list** | [**List[AlarmSearchStatus]**](AlarmSearchStatus.md) |  | [optional] |
| **severity_list** | [**List[AlarmSeverity]**](AlarmSeverity.md) |  | [optional] |
| **assignee_id** | [**UserId**](UserId.md) |  | [optional] |
| **search_propagated_alarms** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type_list`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmFilterConfig.model_validate(data)` or `AlarmFilterConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

