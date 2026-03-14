
# OAuth2BasicMapperConfig

`tb_ce_client.models.OAuth2BasicMapperConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **email_attribute_key** | **str** | Email attribute key of OAuth2 principal attributes. Must be specified for BASIC mapper type and cannot be specified for GITHUB type | [optional] |
| **first_name_attribute_key** | **str** | First name attribute key | [optional] |
| **last_name_attribute_key** | **str** | Last name attribute key | [optional] |
| **tenant_name_strategy** | [**TenantNameStrategyType**](TenantNameStrategyType.md) | Tenant naming strategy. For DOMAIN type, domain for tenant name will be taken from the email (substring before '@') | |
| **tenant_name_pattern** | **str** | Tenant name pattern for CUSTOM naming strategy. OAuth2 attributes in the pattern can be used by enclosing attribute key in '%{' and '}' | [optional] |
| **customer_name_pattern** | **str** | Customer name pattern. When creating a user on the first OAuth2 log in, if specified, customer name will be used to create or find existing customer in the platform and assign customerId to the user | [optional] |
| **default_dashboard_name** | **str** | Name of the tenant's dashboard to set as default dashboard for newly created user | [optional] |
| **always_full_screen** | **bool** | Whether default dashboard should be open in full screen | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.email_attribute_key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2BasicMapperConfig.model_validate(data)` or `OAuth2BasicMapperConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

