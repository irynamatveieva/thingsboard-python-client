
# RuleChainMetaData

`tb_paas_client.models.RuleChainMetaData`

A JSON value representing the rule chain metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rule_chain_id** | [**RuleChainId**](RuleChainId.md) | JSON object with Rule Chain Id. | [readonly] |
| **version** | **int** | Version of the Rule Chain | [optional] |
| **first_node_index** | **int** | Index of the first rule node in the 'nodes' list | |
| **nodes** | [**List[RuleNode]**](RuleNode.md) | List of rule node JSON objects | |
| **connections** | [**List[NodeConnectionInfo]**](NodeConnectionInfo.md) | List of JSON objects that represent connections between rule nodes | |
| **rule_chain_connections** | [**List[RuleChainConnectionInfo]**](RuleChainConnectionInfo.md) | List of JSON objects that represent connections between rule nodes and other rule chains. | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.rule_chain_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainMetaData.model_validate(data)` or `RuleChainMetaData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

