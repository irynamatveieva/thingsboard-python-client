
# SimpleCalculatedFieldConfiguration

`tb_pe_client.models.SimpleCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **expression** | **str** |  | [optional] |
| **use_latest_ts** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SimpleCalculatedFieldConfiguration.model_validate(data)` or `SimpleCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

