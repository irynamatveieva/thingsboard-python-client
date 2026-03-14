
# JwtPair

`tb_ce_client.models.JwtPair`

JWT Pair

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **token** | **str** | The JWT Access Token. Used to perform API calls. | [optional] |
| **refresh_token** | **str** | The JWT Refresh Token. Used to get new JWT Access Token if old one has expired. | [optional] |
| **scope** | [**Authority**](Authority.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.token`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `JwtPair.model_validate(data)` or `JwtPair.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

