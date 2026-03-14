
# TrendzSynchronizationResult

`tb_paas_client.models.TrendzSynchronizationResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version** | **str** |  | [optional] |
| **updated_ts** | **int** |  | [optional] |
| **type** | [**TrendzSynchronizationResultType**](TrendzSynchronizationResultType.md) |  | [optional] |
| **status** | [**TrendzSynchronizationStatus**](TrendzSynchronizationStatus.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.version`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzSynchronizationResult.model_validate(data)` or `TrendzSynchronizationResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

