
# NodeConnectionInfo

`tb_pe_client.models.NodeConnectionInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **from_index** | **int** | Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection. | |
| **to_index** | **int** | Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'to' part of the connection. | |
| **type** | **str** | Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure' | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.from_index`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NodeConnectionInfo.model_validate(data)` or `NodeConnectionInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

