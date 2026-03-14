
# PropagationCalculatedFieldConfiguration

`tb_ce_client.models.PropagationCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **expression** | **str** |  | [optional] |
| **relation** | [**RelationPathLevel**](RelationPathLevel.md) |  | |
| **apply_expression_to_resolved_arguments** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PropagationCalculatedFieldConfiguration.model_validate(data)` or `PropagationCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

