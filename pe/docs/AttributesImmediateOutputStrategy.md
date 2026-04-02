
# AttributesImmediateOutputStrategy

`tb_pe_client.models.AttributesImmediateOutputStrategy`

**Extends:** **AttributesOutputStrategy**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **send_attributes_updated_notification** | **bool** |  | [optional] |
| **update_attributes_only_on_value_change** | **bool** |  | [optional] |
| **save_attribute** | **bool** |  | [optional] |
| **send_ws_update** | **bool** |  | [optional] |
| **process_cfs** | **bool** |  | [optional] |



## Referenced Types

#### AttributesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AttributesRuleChainOutputStrategy  *(extends AttributesOutputStrategy, type=`RULE_CHAIN`)*
*See AttributesOutputStrategy for properties.*

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.send_attributes_updated_notification`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AttributesImmediateOutputStrategy.model_validate(data)` or `AttributesImmediateOutputStrategy.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

