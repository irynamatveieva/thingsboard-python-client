
# JobConfiguration

`tb_ce_client.models.JobConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tasks_key** | **str** |  | |
| **to_reprocess** | [**List[TaskResult]**](TaskResult.md) |  | [optional] |
| **type** | **str** |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.tasks_key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `JobConfiguration.model_validate(data)` or `JobConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

