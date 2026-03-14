
# Edge

`tb_ce_client.models.Edge`

A JSON value representing the edge.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EdgeId**](EdgeId.md) | JSON object with the Edge Id. Specify this field to update the Edge. Referencing non-existing Edge Id will cause error. Omit this field to create new Edge. | [optional] |
| **created_time** | **int** | Timestamp of the edge creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Use 'assignDeviceToTenant' to change the Tenant Id. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. Use 'assignEdgeToCustomer' to change the Customer Id. | [optional] [readonly] |
| **root_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | JSON object with Root Rule Chain Id. Use 'setEdgeRootRuleChain' to change the Root Rule Chain Id. | [optional] [readonly] |
| **name** | **str** | Unique Edge Name in scope of Tenant | |
| **type** | **str** | Edge type | |
| **label** | **str** | Label that may be used in widgets | [optional] |
| **routing_key** | **str** | Edge routing key ('username') to authorize on cloud | |
| **secret** | **str** | Edge secret ('password') to authorize on cloud | |
| **version** | **int** |  | [optional] |
| **additional_info** | **object** | Additional parameters of the edge. May include: 'description' (string). | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Edge.model_validate(data)` or `Edge.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

