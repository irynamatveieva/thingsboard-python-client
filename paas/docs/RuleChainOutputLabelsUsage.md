
# RuleChainOutputLabelsUsage

`tb_paas_client.models.RuleChainOutputLabelsUsage`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Rule Chain Id | [readonly] |
| **rule_node_id** | [**RuleNodeId**](RuleNodeId.md) | Rule Node Id | [readonly] |
| **rule_chain_name** | **str** | Rule Chain Name | [readonly] |
| **rule_node_name** | **str** | Rule Node Name | [readonly] |
| **labels** | **List[str]** | Output labels | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.rule_chain_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainOutputLabelsUsage.model_validate(data)` or `RuleChainOutputLabelsUsage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

