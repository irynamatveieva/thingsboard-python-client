
# OAuth2MapperConfig

`tb_ce_client.models.OAuth2MapperConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **allow_user_creation** | **bool** | Whether user should be created if not yet present on the platform after successful authentication | [optional] |
| **activate_user** | **bool** | Whether user credentials should be activated when user is created after successful authentication | [optional] |
| **type** | [**MapperType**](MapperType.md) | Type of OAuth2 mapper. Depending on this param, different mapper config fields must be specified | |
| **basic** | [**OAuth2BasicMapperConfig**](OAuth2BasicMapperConfig.md) | Mapper config for BASIC and GITHUB mapper types | [optional] |
| **custom** | [**OAuth2CustomMapperConfig**](OAuth2CustomMapperConfig.md) | Mapper config for CUSTOM mapper type | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.allow_user_creation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2MapperConfig.model_validate(data)` or `OAuth2MapperConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

