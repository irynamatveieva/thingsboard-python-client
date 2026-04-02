
# RuleChain

`tb_paas_client.models.RuleChain`

A JSON value representing the rule chain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**RuleChainId**](RuleChainId.md) | JSON object with the Rule Chain Id. Specify this field to update the Rule Chain. Referencing non-existing Rule Chain Id will cause error. Omit this field to create new rule chain. | [optional] |
| **created_time** | **int** | Timestamp of the rule chain creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [readonly] |
| **name** | **str** | Rule Chain name | |
| **type** | [**RuleChainType**](RuleChainType.md) | Rule Chain type. 'EDGE' rule chains are processing messages on the edge devices only. | [optional] |
| **first_rule_node_id** | [**RuleNodeId**](RuleNodeId.md) | JSON object with Rule Chain Id. Pointer to the first rule node that should receive all messages pushed to this rule chain. | [optional] |
| **root** | **bool** | Indicates root rule chain. The root rule chain process messages from all devices and entities by default. User may configure default rule chain per device profile. | [optional] |
| **debug_mode** | **bool** | Reserved for future usage. | [optional] |
| **configuration** | **object** |  | [optional] |
| **version** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChain.model_validate(data)` or `RuleChain.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

