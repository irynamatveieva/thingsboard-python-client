
# DummyTaskResult

`tb_paas_client.models.DummyTaskResult`

**Extends:** **TaskResult**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **failure** | [**DummyTaskFailure**](DummyTaskFailure.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.failure`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DummyTaskResult.model_validate(data)` or `DummyTaskResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

