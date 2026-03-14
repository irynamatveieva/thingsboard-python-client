
# DummyTaskFailure

`tb_ce_client.models.DummyTaskFailure`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error** | **str** |  | [optional] |
| **number** | **int** |  | [optional] |
| **fail_always** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.error`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DummyTaskFailure.model_validate(data)` or `DummyTaskFailure.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

