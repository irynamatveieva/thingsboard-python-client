
# AggKeyInput

`tb_pe_client.models.AggKeyInput`

**Extends:** **AggInput**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | **str** |  | [optional] |



## Referenced Types

#### AggInput
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AggFunctionInput  *(extends AggInput, type=`function`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| function | str |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AggKeyInput.model_validate(data)` or `AggKeyInput.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

