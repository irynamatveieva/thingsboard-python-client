
# AlarmCalculatedFieldConfiguration

`tb_pe_client.models.AlarmCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **create_rules** | [**Dict[str, AlarmRuleDefinition]**](AlarmRuleDefinition.md) |  | |
| **clear_rule** | [**AlarmRuleDefinition**](AlarmRuleDefinition.md) |  | [optional] |
| **propagate** | **bool** |  | [optional] |
| **propagate_to_owner** | **bool** |  | [optional] |
| **propagate_to_owner_hierarchy** | **bool** |  | [optional] |
| **propagate_to_tenant** | **bool** |  | [optional] |
| **propagate_relation_types** | **List[str]** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmCalculatedFieldConfiguration.model_validate(data)` or `AlarmCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

