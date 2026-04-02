
# OAuth2MapperConfig

`tb_pe_client.models.OAuth2MapperConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **allow_user_creation** | **bool** | Whether user should be created if not yet present on the platform after successful authentication | [optional] |
| **activate_user** | **bool** | Whether user credentials should be activated when user is created after successful authentication | [optional] |
| **type** | [**MapperType**](MapperType.md) | Type of OAuth2 mapper. Depending on this param, different mapper config fields must be specified | |
| **basic** | [**OAuth2BasicMapperConfig**](OAuth2BasicMapperConfig.md) | Mapper config for BASIC and GITHUB mapper types | [optional] |
| **custom** | [**OAuth2CustomMapperConfig**](OAuth2CustomMapperConfig.md) | Mapper config for CUSTOM mapper type | [optional] |



## Referenced Types

#### MapperType (enum)
`BASIC` | `CUSTOM` | `GITHUB` | `APPLE`

#### OAuth2BasicMapperConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| email_attribute_key | str | Email attribute key of OAuth2 principal attributes. Must be specified for BASIC mapper type and cannot be specified for GITHUB type | [optional] |
| first_name_attribute_key | str | First name attribute key | [optional] |
| last_name_attribute_key | str | Last name attribute key | [optional] |
| tenant_name_strategy | TenantNameStrategyType | Tenant naming strategy. For DOMAIN type, domain for tenant name will be taken from the email (substring before '@') |  |
| tenant_name_pattern | str | Tenant name pattern for CUSTOM naming strategy. OAuth2 attributes in the pattern can be used by enclosing attribute key in '%{' and '}' | [optional] |
| customer_name_pattern | str | Customer name pattern. When creating a user on the first OAuth2 log in, if specified, customer name will be used to create or find existing customer in the platform and assign customerId to the user | [optional] |
| default_dashboard_name | str | Name of the tenant's dashboard to set as default dashboard for newly created user | [optional] |
| always_full_screen | bool | Whether default dashboard should be open in full screen | [optional] |
| parent_customer_name_pattern | str |  | [optional] |
| user_groups_name_pattern | List[str] |  | [optional] |

#### OAuth2CustomMapperConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| url | str |  | [optional] |
| username | str |  | [optional] |
| password | str |  | [optional] |
| send_token | bool |  | [optional] |

#### TenantNameStrategyType (enum)
`DOMAIN` | `EMAIL` | `CUSTOM`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.allow_user_creation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2MapperConfig.model_validate(data)` or `OAuth2MapperConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

