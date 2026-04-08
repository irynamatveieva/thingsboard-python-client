
# OAuth2ClientRegistrationTemplate

`tb_ce_client.models.OAuth2ClientRegistrationTemplate`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**OAuth2ClientRegistrationTemplateId**](OAuth2ClientRegistrationTemplateId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **additional_info** | **object** |  | [optional] |
| **provider_id** | **str** | OAuth2 provider identifier (e.g. its name) | |
| **mapper_config** | [**OAuth2MapperConfig**](OAuth2MapperConfig.md) | Default config for mapping OAuth2 log in response to platform entities | [optional] |
| **authorization_uri** | **str** | Default authorization URI of the OAuth2 provider | [optional] |
| **access_token_uri** | **str** | Default access token URI of the OAuth2 provider | [optional] |
| **scope** | **List[str]** | Default OAuth scopes that will be requested from OAuth2 platform | [optional] |
| **user_info_uri** | **str** | Default user info URI of the OAuth2 provider | [optional] |
| **user_name_attribute_name** | **str** | Default name of the username attribute in OAuth2 provider log in response | [optional] |
| **jwk_set_uri** | **str** | Default JSON Web Key URI of the OAuth2 provider | [optional] |
| **client_authentication_method** | **str** | Default client authentication method to use: 'BASIC' or 'POST' | [optional] |
| **comment** | **str** | Comment for OAuth2 provider | [optional] |
| **login_button_icon** | **str** | Default log in button icon for OAuth2 provider | [optional] |
| **login_button_label** | **str** | Default OAuth2 provider label | [optional] |
| **help_link** | **str** | Help link for OAuth2 provider | [optional] |
| **name** | **str** |  | [optional] |



## Referenced Types

#### OAuth2ClientRegistrationTemplateId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### OAuth2MapperConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| allow_user_creation | bool | Whether user should be created if not yet present on the platform after successful authentication | [optional] |
| activate_user | bool | Whether user credentials should be activated when user is created after successful authentication | [optional] |
| type | MapperType | Type of OAuth2 mapper. Depending on this param, different mapper config fields must be specified |  |
| basic | OAuth2BasicMapperConfig | Mapper config for BASIC and GITHUB mapper types | [optional] |
| custom | OAuth2CustomMapperConfig | Mapper config for CUSTOM mapper type | [optional] |

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

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2ClientRegistrationTemplate.model_validate(data)` or `OAuth2ClientRegistrationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

