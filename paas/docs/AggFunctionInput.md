
# AggFunctionInput

`tb_paas_client.models.AggFunctionInput`

**Extends:** **AggInput**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **function** | **str** |  | [optional] |



## Referenced Types

#### AggInput
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.function`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AggFunctionInput.model_validate(data)` or `AggFunctionInput.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

