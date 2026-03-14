
# ClaimRequest

`tb_ce_client.models.ClaimRequest`

Claiming request which can optionally contain secret key

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **secret_key** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.secret_key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ClaimRequest.model_validate(data)` or `ClaimRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

