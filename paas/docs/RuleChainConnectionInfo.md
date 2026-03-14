
# RuleChainConnectionInfo

`tb_paas_client.models.RuleChainConnectionInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **from_index** | **int** | Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection. | |
| **target_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | JSON object with the Rule Chain Id. | |
| **additional_info** | **object** | JSON object with the additional information about the connection. | |
| **type** | **str** | Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure' | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.from_index`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainConnectionInfo.model_validate(data)` or `RuleChainConnectionInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

