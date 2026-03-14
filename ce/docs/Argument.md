
# Argument

`tb_ce_client.models.Argument`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **ref_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **ref_dynamic_source_configuration** | [**CfArgumentDynamicSourceConfiguration**](CfArgumentDynamicSourceConfiguration.md) |  | [optional] |
| **ref_entity_key** | [**ReferencedEntityKey**](ReferencedEntityKey.md) |  | [optional] |
| **default_value** | **str** |  | [optional] |
| **limit** | **int** |  | [optional] |
| **time_window** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.ref_entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Argument.model_validate(data)` or `Argument.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

