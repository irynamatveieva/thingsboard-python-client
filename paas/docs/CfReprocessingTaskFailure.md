
# CfReprocessingTaskFailure

`tb_paas_client.models.CfReprocessingTaskFailure`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error** | **str** |  | [optional] |
| **entity_info** | [**EntityInfo**](EntityInfo.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.error`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CfReprocessingTaskFailure.model_validate(data)` or `CfReprocessingTaskFailure.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

