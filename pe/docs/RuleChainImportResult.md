
# RuleChainImportResult

`tb_pe_client.models.RuleChainImportResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rule_chain_id** | [**RuleChainId**](RuleChainId.md) |  | [optional] |
| **rule_chain_name** | **str** |  | [optional] |
| **updated** | **bool** |  | [optional] |
| **error** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.rule_chain_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainImportResult.model_validate(data)` or `RuleChainImportResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

