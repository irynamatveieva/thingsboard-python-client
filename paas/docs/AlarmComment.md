
# AlarmComment

`tb_paas_client.models.AlarmComment`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AlarmCommentId**](AlarmCommentId.md) | JSON object with the alarm comment Id. Specify this field to update the alarm comment. Referencing non-existing alarm Id will cause error. Omit this field to create new alarm. | [optional] |
| **created_time** | **int** | Timestamp of the alarm comment creation, in milliseconds | [optional] [readonly] |
| **alarm_id** | [**AlarmId**](AlarmId.md) | JSON object with Alarm id. | [optional] [readonly] |
| **user_id** | [**UserId**](UserId.md) | JSON object with User id. | [optional] [readonly] |
| **type** | [**AlarmCommentType**](AlarmCommentType.md) | Defines origination of comment. System type means comment was created by TB. OTHER type means comment was created by user. | [optional] |
| **comment** | **object** | JSON object with text of comment. | [optional] |
| **name** | **str** | representing comment text | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmComment.model_validate(data)` or `AlarmComment.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

