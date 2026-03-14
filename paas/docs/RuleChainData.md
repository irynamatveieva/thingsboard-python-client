
# RuleChainData

`tb_paas_client.models.RuleChainData`

A JSON value representing the rule chains.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rule_chains** | [**List[RuleChain]**](RuleChain.md) | List of the Rule Chain objects. | |
| **metadata** | [**List[RuleChainMetaData]**](RuleChainMetaData.md) | List of the Rule Chain metadata objects. | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.rule_chains`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainData.model_validate(data)` or `RuleChainData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

