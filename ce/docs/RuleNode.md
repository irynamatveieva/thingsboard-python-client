
# RuleNode

`tb_ce_client.models.RuleNode`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**RuleNodeId**](RuleNodeId.md) | JSON object with the Rule Node Id. Specify this field to update the Rule Node. Referencing non-existing Rule Node Id will cause error. Omit this field to create new rule node. | [optional] |
| **created_time** | **int** | Timestamp of the rule node creation, in milliseconds | [optional] [readonly] |
| **rule_chain_id** | [**RuleChainId**](RuleChainId.md) | JSON object with the Rule Chain Id.  | [optional] [readonly] |
| **type** | **str** | Full Java Class Name of the rule node implementation.  | [optional] |
| **name** | **str** | User defined name of the rule node. Used on UI and for logging.  | [optional] |
| **debug_settings** | [**DebugSettings**](DebugSettings.md) | Debug settings object. | [optional] |
| **singleton_mode** | **bool** | Enable/disable singleton mode.  | [optional] |
| **queue_name** | **str** | Queue name.  | [optional] |
| **configuration_version** | **int** | Version of rule node configuration.  | [optional] |
| **configuration** | **object** | JSON with the rule node configuration. Structure depends on the rule node implementation. | [optional] |
| **external_id** | [**RuleNodeId**](RuleNodeId.md) |  | [optional] |
| **additional_info** | **object** | Additional parameters of the rule node. May include: 'layoutX' (number, X coordinate for visualization), 'layoutY' (number, Y coordinate for visualization), 'description' (string). | [optional] |
| **debug_mode** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleNode.model_validate(data)` or `RuleNode.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

