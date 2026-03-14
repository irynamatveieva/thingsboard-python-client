
# TelemetryObserveStrategy

`tb_ce_client.models.TelemetryObserveStrategy`

## Enum Values


* `SINGLE_LEFT_PARENTHESIS_0_RIGHT_PARENTHESIS_COLON__ONE_RESOURCE_EQUALS_ONE_SINGLE_OBSERVE_REQUEST` (value: `'SINGLE (0): One resource equals one single observe request'`)

* `COMPOSITE_ALL_LEFT_PARENTHESIS_1_RIGHT_PARENTHESIS_COLON__ALL_RESOURCES_IN_ONE_COMPOSITE_OBSERVE_REQUEST` (value: `'COMPOSITE_ALL (1): All resources in one composite observe request'`)

* `COMPOSITE_BY_OBJECT_LEFT_PARENTHESIS_2_RIGHT_PARENTHESIS_COLON__GROUPED_COMPOSITE_OBSERVE_REQUESTS_BY_OBJECT` (value: `'COMPOSITE_BY_OBJECT (2): Grouped composite observe requests by object'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TelemetryObserveStrategy.model_validate(data)` or `TelemetryObserveStrategy.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

