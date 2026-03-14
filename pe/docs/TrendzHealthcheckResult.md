
# TrendzHealthcheckResult

`tb_pe_client.models.TrendzHealthcheckResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version** | **str** |  | [optional] |
| **type** | [**TrendzSynchronizationResultType**](TrendzSynchronizationResultType.md) |  | [optional] |
| **status** | [**TrendzSynchronizationStatus**](TrendzSynchronizationStatus.md) |  | [optional] |
| **message** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.version`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzHealthcheckResult.model_validate(data)` or `TrendzHealthcheckResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

