
# AlarmAssignee

`tb_pe_client.models.AlarmAssignee`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**UserId**](UserId.md) |  | [optional] |
| **first_name** | **str** |  | [optional] |
| **last_name** | **str** |  | [optional] |
| **email** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmAssignee.model_validate(data)` or `AlarmAssignee.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

