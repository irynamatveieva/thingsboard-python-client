
# CalculatedField

`tb_pe_client.models.CalculatedField`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**CalculatedFieldId**](CalculatedFieldId.md) | JSON object with the Calculated Field Id. Referencing non-existing Calculated Field Id will cause error. | [optional] |
| **created_time** | **int** | Timestamp of the calculated field creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **type** | [**CalculatedFieldType**](CalculatedFieldType.md) |  | [optional] |
| **name** | **str** | User defined name of the calculated field. | [optional] |
| **debug_settings** | [**DebugSettings**](DebugSettings.md) | Debug settings object. | [optional] |
| **configuration_version** | **int** | Version of calculated field configuration. | [optional] |
| **configuration** | [**CalculatedFieldConfiguration**](CalculatedFieldConfiguration.md) |  | |
| **version** | **int** |  | [optional] |
| **additional_info** | **object** | Additional parameters of the calculated field | [optional] |
| **debug_mode** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CalculatedField.model_validate(data)` or `CalculatedField.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

