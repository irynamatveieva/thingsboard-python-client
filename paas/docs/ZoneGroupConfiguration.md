
# ZoneGroupConfiguration

`tb_paas_client.models.ZoneGroupConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **perimeter_key_name** | **str** |  | |
| **report_strategy** | [**GeofencingReportStrategy**](GeofencingReportStrategy.md) |  | |
| **create_relations_with_matched_zones** | **bool** |  | [optional] |
| **ref_entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **ref_dynamic_source_configuration** | [**CfArgumentDynamicSourceConfiguration**](CfArgumentDynamicSourceConfiguration.md) |  | [optional] |
| **relation_type** | **str** |  | [optional] |
| **direction** | [**EntitySearchDirection**](EntitySearchDirection.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.perimeter_key_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ZoneGroupConfiguration.model_validate(data)` or `ZoneGroupConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

