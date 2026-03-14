
# DefaultRuleChainCreateRequest

`tb_paas_client.models.DefaultRuleChainCreateRequest`

A JSON value representing the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | Name of the new rule chain | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DefaultRuleChainCreateRequest.model_validate(data)` or `DefaultRuleChainCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

